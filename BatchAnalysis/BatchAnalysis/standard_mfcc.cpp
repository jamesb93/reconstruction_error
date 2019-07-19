#include <iostream>
#include "algorithmfactory.h"
#include "scheduler/network.h"
#include "streaming/algorithms/poolstorage.h"
#include "dirent.h"
#include "sys/stat.h"

using namespace std;
using namespace essentia;
using namespace essentia::streaming;
using namespace essentia::scheduler;

int main(int argc, char* argv[]) {
    // register the algorithms in the factory(ies)
    essentia::init();

    /////// PARAMS //////////////
    int framesize = 4096;
    int hopsize = 1024;
    int sr = 44100;
    vector<string> statistics = {
        "min",
        "max",
        "median",
        "mean",
        "var",
        "stdev",
        "skew",
        "kurt",
        "dmean",
        "dvar",
        "dmean2",
        "dvar2",
    };
    
    // instanciate facgory and create algorithms:
    streaming::AlgorithmFactory& factory = streaming::AlgorithmFactory::instance();

    Algorithm* audioload        = factory.create("MonoLoader",
                                           "sampleRate", sr,
                                           "downmix", "mix");
    Algorithm* frameCutter      = factory.create("FrameCutter",
                                           "frameSize", framesize,
                                           "hopSize", hopsize,
                                           "startFromZero", true );
    Algorithm* window           = factory.create("Windowing", "type", "hann");
    Algorithm* spectrum         = factory.create("Spectrum");
    Algorithm* yin              = factory.create("PitchYinFFT", "frameSize", framesize, "sampleRate", sr);
    Algorithm* specPeaks        = factory.create("SpectralPeaks", "minFrequency", 1);
    Algorithm* dissonance       = factory.create("Dissonance");
    Algorithm* harmPeaks        = factory.create("HarmonicPeaks");
    Algorithm* hpcp             = factory.create("HPCP");
    Algorithm* tristim          = factory.create("Tristimulus");
    Algorithm* inharm           = factory.create("Inharmonicity");
    Algorithm* oddToEven        = factory.create("OddToEvenHarmonicEnergyRatio");
    Algorithm* specContrast     = factory.create("SpectralContrast", "frameSize", framesize);
    Algorithm* specComplexity   = factory.create("SpectralComplexity");
    Algorithm* pitchSalience    = factory.create("PitchSalience");
    Algorithm* strongPeak       = factory.create("StrongPeak");
    Algorithm* flux             = factory.create("Flux");
    Algorithm* flatness         = factory.create("FlatnessDB");
    Algorithm* rms              = factory.create("RMS");
    Algorithm* moments          = factory.create("CentralMoments");
    Algorithm* rolloff          = factory.create("RollOff");
    Algorithm* decrease         = factory.create("Decrease");
    Algorithm* hfc              = factory.create("HFC");
    Algorithm* zc               = factory.create("ZeroCrossingRate");
    Algorithm* energy           = factory.create("Energy");
    Algorithm* hpcpEntropy      = factory.create("Entropy");
    Algorithm* entropy          = factory.create("Entropy");
    Algorithm* hpcpCrest        = factory.create("Crest");
    Algorithm* crest            = factory.create("Crest");
    Algorithm* dynComplexity    = factory.create("DynamicComplexity");
    Algorithm* mfcc             = factory.create("MFCC");
    // Envelope Based Stuff
    Algorithm* envelope         = factory.create("Envelope");
    Algorithm* maxToTotal       = factory.create("MaxToTotal");
    Algorithm* minToTotal       = factory.create("MinToTotal");
    Algorithm* TCToTotal        = factory.create("TCToTotal");
    
    
    // data storage
    Pool pool;

    /////////// CONNECTING THE ALGORITHMS ////////////////
    cout << "-------- connecting algos --------" << endl;

    // audio -> framecutter
    audioload->output("audio")              >>  frameCutter->input("signal");

    // Spectrum
    frameCutter->output("frame")            >>  window->input("frame");
    window->output("frame")                 >>  spectrum->input("frame");
    
    // MFCC
    spectrum->output("spectrum")            >>  mfcc->input("spectrum");
    mfcc->output("bands")                   >>  PC(pool, "mfcc_bands");
    mfcc->output("mfcc")                    >>  PC(pool, "mfcc_coeffs");

    // YIN
    spectrum->output("spectrum")            >>  yin->input("spectrum");
    yin->output("pitch")                    >>  PC(pool, "fundamental");
    yin->output("pitchConfidence")          >>  PC(pool, "pitch_confidence");

    // Spectral Peaks
    spectrum->output("spectrum")            >>  specPeaks->input("spectrum");

    // Spectral Complexity
    spectrum->output("spectrum")                    >>  specComplexity->input("spectrum");
    specComplexity->output("spectralComplexity")    >> PC(pool, "spectralComplexity");

    // Spectral Contrast
    spectrum->output("spectrum")                >>  specContrast->input("spectrum");
    specContrast->output("spectralContrast")    >>  PC(pool, "SpectralContrast");
    specContrast->output("spectralValley")      >>  PC(pool, "SpectralValley");

    //Spectral Crest
    spectrum->output("spectrum")            >>  crest->input("array");
    crest->output("crest")                  >>  PC(pool, "spectralCrest");

    // Spectral Energy
    spectrum->output("spectrum")            >>  energy->input("array");
    energy->output("energy")                >>  PC(pool, "spectralEnergy");

    // Spectral Entropy
    spectrum->output("spectrum")            >>  entropy->input("array");
    entropy->output("entropy")              >>  PC(pool, "spectralEntropy");

    // Spectral Rolloff
    spectrum->output("spectrum")            >>  rolloff->input("spectrum");
    rolloff->output("rollOff")              >>  PC(pool, "rollOff");

    // Spectral Flatness
    spectrum->output("spectrum")            >>  flatness->input("array");
    flatness->output("flatnessDB")          >>  PC(pool, "spectralFlatnessMeasure");

    // Spectral Moments
    spectrum->output("spectrum")            >>  moments->input("array");
    moments->output("centralMoments")       >>  PC(pool, "spectralMoments");

    // Spectral Decrease
    spectrum->output("spectrum")            >>  decrease->input("array");
    decrease->output("decrease")            >>  PC(pool, "spectralDecrease");
    
    // HFC
    spectrum->output("spectrum")            >>  hfc->input("spectrum");
    hfc->output("hfc")                      >>  PC(pool, "hfc");

    // Strong Peak
    spectrum->output("spectrum")            >>  strongPeak->input("spectrum");
    strongPeak->output("strongPeak")        >>  PC(pool, "strongPeak");

    // Flux
    spectrum->output("spectrum")            >>  flux->input("spectrum");
    flux->output("flux")                    >>  PC(pool, "spectralFlux");

    // Pitch Salience
    spectrum->output("spectrum")            >>  pitchSalience->input("spectrum");
    pitchSalience->output("pitchSalience")  >>  PC(pool, "pitchSalience");
    
    // Dissonance
    specPeaks->output("frequencies")        >>  dissonance->input("frequencies");
    specPeaks->output("magnitudes")         >>  dissonance->input("magnitudes");
    dissonance->output("dissonance")        >>  PC(pool, "dissonance");
    
    // Harmonic Peaks
    specPeaks->output("frequencies")        >>  harmPeaks->input("frequencies");
    specPeaks->output("magnitudes")         >>  harmPeaks->input("magnitudes");
    yin->output("pitch")                    >>  harmPeaks->input("pitch");

    // Tristimulus
    harmPeaks->output("harmonicFrequencies")          >>  tristim->input("frequencies");
    harmPeaks->output("harmonicMagnitudes")           >>  tristim->input("magnitudes");
    tristim->output("tristimulus")                    >>  PC(pool, "tristimulus");

    // Inharmonicity
    harmPeaks->output("harmonicFrequencies")          >>  inharm->input("frequencies");
    harmPeaks->output("harmonicMagnitudes")           >>  inharm->input("magnitudes");
    inharm->output("inharmonicity")                   >>  PC(pool, "inharmonicity");
    
    // OddToEvenHarmonicEnergyRatio
    harmPeaks->output("harmonicFrequencies")          >>  oddToEven->input("frequencies");
    harmPeaks->output("harmonicMagnitudes")           >>  oddToEven->input("magnitudes");
    oddToEven->output("oddToEvenHarmonicEnergyRatio") >> PC(pool, "oddtoeven");
    
    // RMS
    frameCutter->output("frame")            >>  rms->input("array");
    rms->output("rms")                      >>  PC(pool, "rms");

    // HPCP
    specPeaks->output("frequencies")        >>  hpcp->input("frequencies");
    specPeaks->output("magnitudes")         >>  hpcp->input("magnitudes");
    hpcp->output("hpcp")                    >>  PC(pool, "hpcp");

    // Zero Crossing
    frameCutter->output("frame")            >>  zc->input("signal");
    zc->output("zeroCrossingRate")          >>  PC(pool, "zeroCrossingRate");

    // Dynamic Complexity
    audioload->output("audio")                  >>  dynComplexity->input("signal");
    dynComplexity->output("dynamicComplexity")  >>  PC(pool, "dynamicComplexity");
    dynComplexity->output("loudness")           >>  PC(pool, "loudness");
    
//    // ToToTotal
//    audioload->output("audio")              >>  envelope->input("signal");
//    envelope->output("signal")              >>  TCToTotal->input("envelope");
//    TCToTotal->output("TCToTotal")          >>  PC(pool, "tctototal");
    
    // MaxToTotal
    envelope->output("signal")              >>  maxToTotal->input("envelope");
    maxToTotal->output("maxToTotal")        >>  PC(pool, "maxtototal");
    
    
    // MinToTotal
    envelope->output("signal")              >>  minToTotal->input("envelope");
    minToTotal->output("minToTotal")        >>  PC(pool, "mintototal");
    
    // HPCP Crest
    hpcp->output("hpcp")                    >>  hpcpCrest->input("array");
    hpcpCrest->output("crest")              >>  PC(pool, "HPCPCrest");
    
    // HPCP Entropy
    hpcp->output("hpcp")                    >>  hpcpEntropy->input("array");
    hpcpEntropy->output("entropy")            >>  PC(pool, "HPCPEntropy");
    
    
    Network n(audioload);
//    cout << "-------- start processing --------" << endl;
    ///////////  START LOOPING AUDIO FILES ///////////
    pool.clear();
    // Navigate a directory
    const char *audioPath = "/Users/jamesbradbury/dev/data_bending/DataAudioUnique";
//    const char *analysisPath = "/Users/jamesbradbury/dev/data_bending/essentia_analysis";
    
    int status;

    struct dirent *entry;
//    struct dirent *data_file;

    DIR *audioFiles;
//    DIR *essentiaAnal;
    audioFiles = opendir(audioPath);
//    essentiaAnal = opendir(analysisPath);
    string inputFile;
    
    double numFiles = 21619;
    double counter = 0;
    while((entry = readdir(audioFiles))) {
        char root[PATH_MAX];
        struct stat buffer;
        sprintf(root, "%s/%s", audioPath, entry->d_name);
        status = lstat(root, &buffer);
        if (S_ISDIR(buffer.st_mode) || entry->d_name[0] == '.') {
            continue;
        }
        else {
            counter += 1;
            cout << counter << "/" << numFiles << endl;
            n.reset();
            audioload->configure("filename", root);
//            cout << "Processing:" << root << endl;
            n.run();

            //// Aggregation ////
            char outputFile[PATH_MAX];
            strcpy(outputFile, "/Users/jamesbradbury/dev/data_bending/essentia_analysis/");
            strcat(outputFile, entry->d_name);
            strcat(outputFile, ".yaml");
//            cout << "-------- writing results to file " << outputFile << " --------" << endl;

            standard::Algorithm* aggregator = standard::AlgorithmFactory::create("PoolAggregator",
                                                                                 "defaultStats", statistics);

            standard::Algorithm* output = standard::AlgorithmFactory::create("YamlOutput",
                                                                             "filename", outputFile);
            Pool poolStats;

            aggregator->input("input").set(pool);
            aggregator->output("output").set(poolStats);
            output->input("pool").set(poolStats);

            aggregator->compute();
            output->compute();

            delete output;
            delete aggregator;
        }
    }
    closedir(audioFiles);
    essentia::shutdown();
    return 0;
}
