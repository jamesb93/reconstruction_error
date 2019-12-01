{
	"patcher" : 	{
		"fileversion" : 1,
		"appversion" : 		{
			"major" : 8,
			"minor" : 1,
			"revision" : 0,
			"architecture" : "x64",
			"modernui" : 1
		}
,
		"classnamespace" : "box",
		"rect" : [ 0.0, 45.0, 1120.0, 1005.0 ],
		"bglocked" : 0,
		"openinpresentation" : 1,
		"default_fontsize" : 12.0,
		"default_fontface" : 0,
		"default_fontname" : "Arial",
		"gridonopen" : 2,
		"gridsize" : [ 15.0, 15.0 ],
		"gridsnaponopen" : 2,
		"objectsnaponopen" : 1,
		"statusbarvisible" : 2,
		"toolbarvisible" : 0,
		"lefttoolbarpinned" : 0,
		"toptoolbarpinned" : 0,
		"righttoolbarpinned" : 0,
		"bottomtoolbarpinned" : 0,
		"toolbars_unpinned_last_save" : 0,
		"tallnewobj" : 0,
		"boxanimatetime" : 200,
		"enablehscroll" : 1,
		"enablevscroll" : 1,
		"devicewidth" : 0.0,
		"description" : "",
		"digest" : "",
		"tags" : "",
		"style" : "",
		"subpatcher_template" : "",
		"boxes" : [ 			{
				"box" : 				{
					"id" : "obj-21",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "bang" ],
					"patching_rect" : [ 473.5, 505.5, 58.0, 22.0 ],
					"text" : "loadbang"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-39",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "signal" ],
					"patching_rect" : [ 390.0, 405.0, 75.0, 22.0 ],
					"text" : "onepole~ 50"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-37",
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 390.0, 345.0, 39.0, 22.0 ],
					"text" : "$1 10"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-30",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "signal", "bang" ],
					"patching_rect" : [ 390.0, 375.0, 34.0, 22.0 ],
					"text" : "line~"
				}

			}
, 			{
				"box" : 				{
					"activebgcolor" : [ 0.203921568627451, 0.752941176470588, 0.784313725490196, 1.0 ],
					"activebgoncolor" : [ 0.647058823529412, 0.647058823529412, 0.647058823529412, 1.0 ],
					"fontface" : 1,
					"fontsize" : 12.0,
					"id" : "obj-20",
					"maxclass" : "live.text",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"parameter_enable" : 1,
					"patching_rect" : [ 390.0, 300.0, 81.0, 30.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 84.5, 230.0, 35.5, 30.0 ],
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_mmax" : 1,
							"parameter_shortname" : "live.text",
							"parameter_enum" : [ "val1", "val2" ],
							"parameter_type" : 2,
							"parameter_longname" : "live.text[6]"
						}

					}
,
					"text" : "Mute",
					"texton" : "Mute",
					"varname" : "live.text[6]"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-19",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 390.0, 270.0, 70.0, 22.0 ],
					"text" : "loadmess 1"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-13",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "signal" ],
					"patching_rect" : [ 156.0, 375.0, 29.5, 22.0 ],
					"text" : "*~"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-14",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "signal" ],
					"patching_rect" : [ 120.0, 375.0, 29.5, 22.0 ],
					"text" : "*~"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-12",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "signal" ],
					"patching_rect" : [ 68.5, 375.0, 29.5, 22.0 ],
					"text" : "*~"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-5",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "signal" ],
					"patching_rect" : [ 13.0, 375.0, 29.5, 22.0 ],
					"text" : "*~"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-38",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "int", "int" ],
					"patching_rect" : [ 315.0, 519.0, 48.0, 22.0 ],
					"text" : "change"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-34",
					"maxclass" : "newobj",
					"numinlets" : 3,
					"numoutlets" : 3,
					"outlettype" : [ "bang", "bang", "" ],
					"patching_rect" : [ 315.0, 554.5, 44.0, 22.0 ],
					"text" : "sel 1 0"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-33",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 315.0, 467.5, 95.0, 22.0 ],
					"text" : "loadmess watch"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-23",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 315.0, 493.5, 87.0, 22.0 ],
					"saved_object_attributes" : 					{
						"filename" : "lockWatch.js",
						"parameter_enable" : 0
					}
,
					"text" : "js lockWatch.js"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-18",
					"linecount" : 3,
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 423.0, 590.5, 105.0, 49.0 ],
					"text" : "window size 0 45 1120 1050, window exec"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-15",
					"linecount" : 4,
					"maxclass" : "message",
					"numinlets" : 2,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 315.0, 590.5, 95.0, 62.0 ],
					"text" : "window size 1302 492 1439 900, window exec"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-2",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 315.0, 659.5, 67.0, 22.0 ],
					"save" : [ "#N", "thispatcher", ";", "#Q", "end", ";" ],
					"text" : "thispatcher"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-87",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 225.0, 249.0, 72.0, 22.0 ],
					"text" : "prepend set"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-84",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"patching_rect" : [ 225.0, 220.0, 118.0, 22.0 ],
					"text" : "route \"Bypass State\""
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-81",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patcher" : 					{
						"fileversion" : 1,
						"appversion" : 						{
							"major" : 8,
							"minor" : 1,
							"revision" : 0,
							"architecture" : "x64",
							"modernui" : 1
						}
,
						"classnamespace" : "box",
						"rect" : [ 59.0, 104.0, 236.0, 237.0 ],
						"bglocked" : 0,
						"openinpresentation" : 0,
						"default_fontsize" : 12.0,
						"default_fontface" : 0,
						"default_fontname" : "Arial",
						"gridonopen" : 1,
						"gridsize" : [ 15.0, 15.0 ],
						"gridsnaponopen" : 1,
						"objectsnaponopen" : 1,
						"statusbarvisible" : 2,
						"toolbarvisible" : 1,
						"lefttoolbarpinned" : 0,
						"toptoolbarpinned" : 0,
						"righttoolbarpinned" : 0,
						"bottomtoolbarpinned" : 0,
						"toolbars_unpinned_last_save" : 0,
						"tallnewobj" : 0,
						"boxanimatetime" : 200,
						"enablehscroll" : 1,
						"enablevscroll" : 1,
						"devicewidth" : 0.0,
						"description" : "",
						"digest" : "",
						"tags" : "",
						"style" : "",
						"subpatcher_template" : "",
						"boxes" : [ 							{
								"box" : 								{
									"id" : "obj-78",
									"maxclass" : "message",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 5.0, 44.0, 42.0, 22.0 ],
									"text" : "get $1"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-73",
									"maxclass" : "newobj",
									"numinlets" : 2,
									"numoutlets" : 2,
									"outlettype" : [ "", "" ],
									"patching_rect" : [ 41.666666666666629, 107.0, 55.0, 22.0 ],
									"text" : "zl slice 1"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-69",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 77.666666666666629, 145.0, 47.0, 22.0 ],
									"text" : "dict.iter"
								}

							}
, 							{
								"box" : 								{
									"data" : 									{
										"LoopBack" : 										{
											"input" : [ 1, 2 ],
											"loopback" : [ 5, 6 ]
										}
,
										"Studio 5" : 										{
											"input" : [ 31, 32 ],
											"loopback" : [ 33, 34 ]
										}
,
										"SPIRAL" : 										{
											"input" : [ 65, 66 ],
											"loopback" : [ 67, 68 ]
										}

									}
,
									"id" : "obj-64",
									"maxclass" : "newobj",
									"numinlets" : 2,
									"numoutlets" : 4,
									"outlettype" : [ "dictionary", "", "", "" ],
									"patching_rect" : [ 5.0, 76.0, 129.0, 22.0 ],
									"saved_object_attributes" : 									{
										"embed" : 1,
										"parameter_enable" : 0,
										"parameter_mappable" : 0
									}
,
									"text" : "dict routing @embed 1"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-60",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 142.666666666666629, 210.0, 80.0, 22.0 ],
									"text" : "s cv.loopback"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-59",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 77.666666666666629, 210.0, 58.0, 22.0 ],
									"text" : "s cv.input"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-56",
									"maxclass" : "newobj",
									"numinlets" : 3,
									"numoutlets" : 3,
									"outlettype" : [ "", "", "" ],
									"patching_rect" : [ 77.666666666666629, 176.0, 149.0, 22.0 ],
									"text" : "route input loopback"
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-80",
									"index" : 1,
									"maxclass" : "inlet",
									"numinlets" : 0,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 5.0, 6.0, 30.0, 30.0 ]
								}

							}
 ],
						"lines" : [ 							{
								"patchline" : 								{
									"destination" : [ "obj-59", 0 ],
									"source" : [ "obj-56", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-60", 0 ],
									"source" : [ "obj-56", 1 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-73", 0 ],
									"source" : [ "obj-64", 1 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-56", 0 ],
									"source" : [ "obj-69", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-69", 0 ],
									"source" : [ "obj-73", 1 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-64", 0 ],
									"source" : [ "obj-78", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-78", 0 ],
									"source" : [ "obj-80", 0 ]
								}

							}
 ]
					}
,
					"patching_rect" : [ 39.5, 590.0, 55.0, 22.0 ],
					"saved_object_attributes" : 					{
						"description" : "",
						"digest" : "",
						"globalpatchername" : "",
						"tags" : ""
					}
,
					"text" : "p routing"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-62",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 211.0, 375.0, 78.0, 22.0 ],
					"text" : "r cv.loopback"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-61",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 13.0, 103.0, 56.0, 22.0 ],
					"text" : "r cv.input"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-55",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 13.5, 480.0, 70.0, 22.0 ],
					"text" : "loadmess 0"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-51",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 92.0, 444.0, 74.0, 20.0 ],
					"text" : "Loop Back",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-50",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 13.5, 444.0, 74.0, 20.0 ],
					"text" : "Monitoring",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-47",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 120.0, 420.0, 55.0, 22.0 ],
					"text" : "dac~"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-41",
					"maxclass" : "newobj",
					"numinlets" : 0,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patcher" : 					{
						"fileversion" : 1,
						"appversion" : 						{
							"major" : 8,
							"minor" : 1,
							"revision" : 0,
							"architecture" : "x64",
							"modernui" : 1
						}
,
						"classnamespace" : "box",
						"rect" : [ 0.0, 0.0, 640.0, 480.0 ],
						"bglocked" : 0,
						"openinpresentation" : 0,
						"default_fontsize" : 12.0,
						"default_fontface" : 0,
						"default_fontname" : "Arial",
						"gridonopen" : 1,
						"gridsize" : [ 15.0, 15.0 ],
						"gridsnaponopen" : 1,
						"objectsnaponopen" : 1,
						"statusbarvisible" : 2,
						"toolbarvisible" : 1,
						"lefttoolbarpinned" : 0,
						"toptoolbarpinned" : 0,
						"righttoolbarpinned" : 0,
						"bottomtoolbarpinned" : 0,
						"toolbars_unpinned_last_save" : 0,
						"tallnewobj" : 0,
						"boxanimatetime" : 200,
						"enablehscroll" : 1,
						"enablevscroll" : 1,
						"devicewidth" : 0.0,
						"description" : "",
						"digest" : "",
						"tags" : "",
						"style" : "",
						"subpatcher_template" : "",
						"boxes" : [ 							{
								"box" : 								{
									"id" : "obj-37",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 50.0, 192.0, 75.0, 22.0 ],
									"text" : "prepend text"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-36",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 50.0, 161.0, 132.0, 22.0 ],
									"text" : "sprintf symout CPU: %i"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-21",
									"maxclass" : "newobj",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "bang" ],
									"patching_rect" : [ 50.0, 100.0, 133.0, 22.0 ],
									"text" : "qmetro 1000 @active 1"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-20",
									"maxclass" : "newobj",
									"numinlets" : 2,
									"numoutlets" : 2,
									"outlettype" : [ "", "int" ],
									"patching_rect" : [ 50.0, 130.0, 77.0, 22.0 ],
									"text" : "adstatus cpu"
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-40",
									"index" : 1,
									"maxclass" : "outlet",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 50.0, 274.0, 30.0, 30.0 ]
								}

							}
 ],
						"lines" : [ 							{
								"patchline" : 								{
									"destination" : [ "obj-36", 0 ],
									"source" : [ "obj-20", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-20", 0 ],
									"source" : [ "obj-21", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-37", 0 ],
									"source" : [ "obj-36", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-40", 0 ],
									"source" : [ "obj-37", 0 ]
								}

							}
 ]
					}
,
					"patching_rect" : [ 99.0, 590.0, 38.0, 22.0 ],
					"saved_object_attributes" : 					{
						"description" : "",
						"digest" : "",
						"globalpatchername" : "",
						"tags" : ""
					}
,
					"text" : "p cpu"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-24",
					"maxclass" : "live.tab",
					"num_lines_patching" : 3,
					"num_lines_presentation" : 4,
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "float" ],
					"parameter_enable" : 1,
					"patching_rect" : [ 13.5, 503.5, 71.0, 73.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 15.0, 322.5, 105.0, 73.0 ],
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_mmax" : 2,
							"parameter_shortname" : "live.tab[2]",
							"parameter_enum" : [ "LoopBack", "Studio 5", "SPIRAL" ],
							"parameter_type" : 2,
							"parameter_unitstyle" : 0,
							"parameter_longname" : "live.tab[2]"
						}

					}
,
					"varname" : "live.tab[2]"
				}

			}
, 			{
				"box" : 				{
					"activebgcolor" : [ 0.647058823529412, 0.647058823529412, 0.647058823529412, 1.0 ],
					"bgcolor" : [ 0.647058823529412, 0.647058823529412, 0.647058823529412, 0.0 ],
					"id" : "obj-17",
					"maxclass" : "live.text",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"parameter_enable" : 1,
					"patching_rect" : [ 143.0, 653.5, 42.0, 19.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 67.0, 29.0, 38.0, 19.0 ],
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_mmax" : 1,
							"parameter_shortname" : "live.text[4]",
							"parameter_enum" : [ "val1", "val2" ],
							"parameter_type" : 2,
							"parameter_longname" : "live.text[5]"
						}

					}
,
					"text" : "RECALL",
					"textoffcolor" : [ 0.137254901960784, 0.137254901960784, 0.137254901960784, 1.0 ],
					"varname" : "live.text[5]"
				}

			}
, 			{
				"box" : 				{
					"activebgcolor" : [ 0.647058823529412, 0.647058823529412, 0.647058823529412, 1.0 ],
					"bgcolor" : [ 0.647058823529412, 0.647058823529412, 0.647058823529412, 0.0 ],
					"id" : "obj-16",
					"maxclass" : "live.text",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"parameter_enable" : 1,
					"patching_rect" : [ 99.0, 653.5, 42.0, 19.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 30.0, 29.0, 38.0, 19.0 ],
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_mmax" : 1,
							"parameter_shortname" : "live.text[4]",
							"parameter_enum" : [ "val1", "val2" ],
							"parameter_type" : 2,
							"parameter_longname" : "live.text[4]"
						}

					}
,
					"text" : "STORE",
					"textoffcolor" : [ 0.137254901960784, 0.137254901960784, 0.137254901960784, 1.0 ],
					"varname" : "live.text[4]"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-9",
					"maxclass" : "live.meter~",
					"numinlets" : 1,
					"numoutlets" : 2,
					"orientation" : 1,
					"outlettype" : [ "float", "int" ],
					"patching_rect" : [ 156.0, 180.5, 100.0, 5.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 15.0, 302.5, 105.0, 18.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-8",
					"maxclass" : "live.meter~",
					"numinlets" : 1,
					"numoutlets" : 2,
					"orientation" : 1,
					"outlettype" : [ "float", "int" ],
					"patching_rect" : [ 156.0, 172.0, 100.0, 5.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 15.0, 282.5, 105.0, 18.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-6",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 13.5, 420.0, 74.0, 22.0 ],
					"text" : "dac~ 1 2"
				}

			}
, 			{
				"box" : 				{
					"fontsize" : 12.0,
					"id" : "obj-48",
					"maxclass" : "live.text",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"parameter_enable" : 1,
					"patching_rect" : [ 229.0, 135.5, 47.0, 23.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 44.0, 205.0, 47.0, 23.0 ],
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_mmax" : 1,
							"parameter_shortname" : "live.text[1]",
							"parameter_enum" : [ "val1", "val2" ],
							"parameter_type" : 2,
							"parameter_longname" : "live.text[3]"
						}

					}
,
					"text" : "open",
					"varname" : "live.text[3]"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-45",
					"maxclass" : "newobj",
					"numinlets" : 4,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patcher" : 					{
						"fileversion" : 1,
						"appversion" : 						{
							"major" : 8,
							"minor" : 1,
							"revision" : 0,
							"architecture" : "x64",
							"modernui" : 1
						}
,
						"classnamespace" : "box",
						"rect" : [ 59.0, 104.0, 640.0, 480.0 ],
						"bglocked" : 0,
						"openinpresentation" : 0,
						"default_fontsize" : 12.0,
						"default_fontface" : 0,
						"default_fontname" : "Arial",
						"gridonopen" : 1,
						"gridsize" : [ 15.0, 15.0 ],
						"gridsnaponopen" : 1,
						"objectsnaponopen" : 1,
						"statusbarvisible" : 2,
						"toolbarvisible" : 1,
						"lefttoolbarpinned" : 0,
						"toptoolbarpinned" : 0,
						"righttoolbarpinned" : 0,
						"bottomtoolbarpinned" : 0,
						"toolbars_unpinned_last_save" : 0,
						"tallnewobj" : 0,
						"boxanimatetime" : 200,
						"enablehscroll" : 1,
						"enablevscroll" : 1,
						"devicewidth" : 0.0,
						"description" : "",
						"digest" : "",
						"tags" : "",
						"style" : "",
						"subpatcher_template" : "",
						"boxes" : [ 							{
								"box" : 								{
									"id" : "obj-2",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 1,
									"outlettype" : [ "bang" ],
									"patching_rect" : [ 346.0, 40.0, 58.0, 22.0 ],
									"text" : "loadbang"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-30",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 135.0, 100.0, 85.0, 22.0 ],
									"text" : "prepend recall"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-27",
									"maxclass" : "newobj",
									"numinlets" : 1,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 50.0, 100.0, 83.0, 22.0 ],
									"text" : "prepend store"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-8",
									"maxclass" : "message",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 521.0, 100.0, 63.0, 22.0 ],
									"text" : "bypass $1"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-6",
									"linecount" : 2,
									"maxclass" : "message",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 346.0, 100.0, 166.0, 35.0 ],
									"text" : "savemode 2, read reverb_settings.json, recall 1"
								}

							}
, 							{
								"box" : 								{
									"id" : "obj-9",
									"linecount" : 3,
									"maxclass" : "message",
									"numinlets" : 2,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 230.0, 100.0, 114.0, 49.0 ],
									"text" : "savemode 2, write reverb_settings.json"
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-38",
									"index" : 1,
									"maxclass" : "inlet",
									"numinlets" : 0,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 50.0, 40.0, 30.0, 30.0 ]
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-39",
									"index" : 2,
									"maxclass" : "inlet",
									"numinlets" : 0,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 135.0, 40.0, 30.0, 30.0 ]
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-40",
									"index" : 3,
									"maxclass" : "inlet",
									"numinlets" : 0,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 230.0, 40.0, 30.0, 30.0 ]
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-42",
									"index" : 4,
									"maxclass" : "inlet",
									"numinlets" : 0,
									"numoutlets" : 1,
									"outlettype" : [ "" ],
									"patching_rect" : [ 521.0, 40.0, 30.0, 30.0 ]
								}

							}
, 							{
								"box" : 								{
									"comment" : "",
									"id" : "obj-43",
									"index" : 1,
									"maxclass" : "outlet",
									"numinlets" : 1,
									"numoutlets" : 0,
									"patching_rect" : [ 86.5, 209.0, 30.0, 30.0 ]
								}

							}
 ],
						"lines" : [ 							{
								"patchline" : 								{
									"destination" : [ "obj-6", 0 ],
									"source" : [ "obj-2", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-43", 0 ],
									"source" : [ "obj-27", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-43", 0 ],
									"source" : [ "obj-30", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-27", 0 ],
									"source" : [ "obj-38", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-30", 0 ],
									"source" : [ "obj-39", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-9", 0 ],
									"source" : [ "obj-40", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-8", 0 ],
									"source" : [ "obj-42", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-43", 0 ],
									"source" : [ "obj-6", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-43", 0 ],
									"source" : [ "obj-8", 0 ]
								}

							}
, 							{
								"patchline" : 								{
									"destination" : [ "obj-43", 0 ],
									"source" : [ "obj-9", 0 ]
								}

							}
 ]
					}
,
					"patching_rect" : [ 156.0, 135.5, 61.0, 22.0 ],
					"saved_object_attributes" : 					{
						"description" : "",
						"digest" : "",
						"globalpatchername" : "",
						"tags" : ""
					}
,
					"text" : "p controls"
				}

			}
, 			{
				"box" : 				{
					"fontsize" : 12.0,
					"id" : "obj-35",
					"maxclass" : "live.text",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"parameter_enable" : 1,
					"patching_rect" : [ 99.0, 616.5, 75.0, 28.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 15.0, 263.0, 105.0, 17.5 ],
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_mmax" : 1,
							"parameter_shortname" : "live.text[2]",
							"parameter_enum" : [ "val1", "val2" ],
							"parameter_type" : 2,
							"parameter_longname" : "live.text[2]"
						}

					}
,
					"text" : "CPU: 4",
					"varname" : "live.text[2]"
				}

			}
, 			{
				"box" : 				{
					"fontsize" : 12.0,
					"id" : "obj-32",
					"maxclass" : "live.text",
					"mode" : 0,
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"parameter_enable" : 1,
					"patching_rect" : [ 237.0, 89.0, 65.0, 36.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 30.0, 135.0, 75.0, 36.0 ],
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_mmax" : 1,
							"parameter_shortname" : "live.text[1]",
							"parameter_enum" : [ "val1", "val2" ],
							"parameter_type" : 2,
							"parameter_longname" : "live.text[1]"
						}

					}
,
					"text" : "write",
					"varname" : "live.text[1]"
				}

			}
, 			{
				"box" : 				{
					"activebgoncolor" : [ 0.337254901960784, 0.607843137254902, 0.341176470588235, 1.0 ],
					"id" : "obj-31",
					"maxclass" : "live.tab",
					"num_lines_patching" : 5,
					"num_lines_presentation" : 5,
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "float" ],
					"parameter_enable" : 1,
					"patching_rect" : [ 186.5, 19.0, 38.0, 83.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 67.0, 50.0, 38.0, 83.0 ],
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_mmax" : 4,
							"parameter_shortname" : "live.tab",
							"parameter_enum" : [ "1", "2", "3", "4", "5" ],
							"parameter_type" : 2,
							"parameter_unitstyle" : 0,
							"parameter_longname" : "live.tab[1]"
						}

					}
,
					"varname" : "live.tab[1]"
				}

			}
, 			{
				"box" : 				{
					"activebgoncolor" : [ 0.996078431372549, 0.192156862745098, 0.192156862745098, 1.0 ],
					"id" : "obj-26",
					"maxclass" : "live.tab",
					"num_lines_patching" : 5,
					"num_lines_presentation" : 5,
					"numinlets" : 1,
					"numoutlets" : 3,
					"outlettype" : [ "", "", "float" ],
					"parameter_enable" : 1,
					"patching_rect" : [ 146.5, 19.0, 38.0, 83.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 30.0, 50.0, 38.0, 83.0 ],
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_mmax" : 4,
							"parameter_shortname" : "live.tab",
							"parameter_enum" : [ "1", "2", "3", "4", "5" ],
							"parameter_type" : 2,
							"parameter_unitstyle" : 0,
							"parameter_longname" : "live.tab"
						}

					}
,
					"varname" : "live.tab"
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-10",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 1,
					"outlettype" : [ "" ],
					"patching_rect" : [ 229.0, 19.0, 70.0, 22.0 ],
					"text" : "loadmess 0"
				}

			}
, 			{
				"box" : 				{
					"activebgoncolor" : [ 0.203921568627451, 0.752941176470588, 0.784313725490196, 1.0 ],
					"fontface" : 1,
					"fontsize" : 12.0,
					"id" : "obj-7",
					"maxclass" : "live.text",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "", "" ],
					"parameter_enable" : 1,
					"patching_rect" : [ 229.0, 48.0, 81.0, 30.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 15.0, 173.0, 105.0, 30.0 ],
					"saved_attribute_attributes" : 					{
						"valueof" : 						{
							"parameter_mmax" : 1,
							"parameter_shortname" : "live.text",
							"parameter_enum" : [ "val1", "val2" ],
							"parameter_type" : 2,
							"parameter_longname" : "live.text"
						}

					}
,
					"text" : "Bypass",
					"texton" : "Bypass",
					"varname" : "live.text"
				}

			}
, 			{
				"box" : 				{
					"fontname" : "Lato Regular",
					"fontsize" : 20.519733870252349,
					"id" : "obj-11",
					"maxclass" : "comment",
					"numinlets" : 1,
					"numoutlets" : 0,
					"patching_rect" : [ 13.0, 14.4, 124.0, 31.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 15.0, 0.0, 105.0, 31.0 ],
					"text" : "CVerb",
					"textjustification" : 1
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-4",
					"maxclass" : "newobj",
					"numinlets" : 2,
					"numoutlets" : 3,
					"outlettype" : [ "signal", "signal", "" ],
					"patching_rect" : [ 13.0, 172.0, 130.0, 22.0 ],
					"text" : "hirt.convolutionreverb~",
					"varname" : "hirt.convolutionreverb~"
				}

			}
, 			{
				"box" : 				{
					"color" : [ 0.329411764705882, 0.784313725490196, 0.847058823529412, 1.0 ],
					"id" : "obj-3",
					"local" : 1,
					"maxclass" : "ezdac~",
					"numinlets" : 2,
					"numoutlets" : 0,
					"patching_rect" : [ 15.0, 686.0, 45.0, 45.0 ],
					"presentation" : 1,
					"presentation_rect" : [ 52.0, 230.0, 31.0, 31.0 ]
				}

			}
, 			{
				"box" : 				{
					"id" : "obj-1",
					"maxclass" : "newobj",
					"numinlets" : 1,
					"numoutlets" : 2,
					"outlettype" : [ "signal", "signal" ],
					"patching_rect" : [ 13.0, 135.5, 55.0, 22.0 ],
					"text" : "adc~ 1 2"
				}

			}
 ],
		"lines" : [ 			{
				"patchline" : 				{
					"destination" : [ "obj-4", 1 ],
					"source" : [ "obj-1", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-4", 0 ],
					"source" : [ "obj-1", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-7", 0 ],
					"source" : [ "obj-10", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-6", 1 ],
					"source" : [ "obj-12", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-47", 1 ],
					"source" : [ "obj-13", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-47", 0 ],
					"source" : [ "obj-14", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-2", 0 ],
					"source" : [ "obj-15", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-2", 0 ],
					"source" : [ "obj-18", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-20", 0 ],
					"source" : [ "obj-19", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-37", 0 ],
					"source" : [ "obj-20", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-15", 0 ],
					"source" : [ "obj-21", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-38", 0 ],
					"source" : [ "obj-23", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-81", 0 ],
					"source" : [ "obj-24", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-45", 0 ],
					"midpoints" : [ 165.5, 105.0, 165.5, 105.0 ],
					"source" : [ "obj-26", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-39", 0 ],
					"source" : [ "obj-30", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-45", 1 ],
					"midpoints" : [ 205.5, 120.0, 179.5, 120.0 ],
					"source" : [ "obj-31", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-45", 2 ],
					"midpoints" : [ 246.5, 120.0, 193.5, 120.0 ],
					"source" : [ "obj-32", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-23", 0 ],
					"source" : [ "obj-33", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-15", 0 ],
					"source" : [ "obj-34", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-18", 0 ],
					"source" : [ "obj-34", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-30", 0 ],
					"source" : [ "obj-37", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-34", 0 ],
					"source" : [ "obj-38", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-12", 1 ],
					"order" : 2,
					"source" : [ "obj-39", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-13", 1 ],
					"order" : 0,
					"source" : [ "obj-39", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 1 ],
					"order" : 1,
					"source" : [ "obj-39", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-5", 1 ],
					"order" : 3,
					"source" : [ "obj-39", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-12", 0 ],
					"midpoints" : [ 78.0, 195.0, 78.0, 195.0 ],
					"order" : 2,
					"source" : [ "obj-4", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-13", 0 ],
					"midpoints" : [ 78.0, 360.0, 165.5, 360.0 ],
					"order" : 0,
					"source" : [ "obj-4", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-14", 0 ],
					"midpoints" : [ 22.5, 360.0, 129.5, 360.0 ],
					"order" : 1,
					"source" : [ "obj-4", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-5", 0 ],
					"midpoints" : [ 22.5, 195.0, 22.5, 195.0 ],
					"order" : 2,
					"source" : [ "obj-4", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-8", 0 ],
					"midpoints" : [ 22.5, 204.0, 153.0, 204.0, 153.0, 168.0, 165.5, 168.0 ],
					"order" : 0,
					"source" : [ "obj-4", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-84", 0 ],
					"midpoints" : [ 133.5, 207.0, 234.5, 207.0 ],
					"source" : [ "obj-4", 2 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-9", 0 ],
					"midpoints" : [ 78.0, 204.0, 153.0, 204.0, 153.0, 177.0, 165.5, 177.0 ],
					"order" : 1,
					"source" : [ "obj-4", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-35", 0 ],
					"source" : [ "obj-41", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-4", 1 ],
					"source" : [ "obj-45", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-4", 1 ],
					"source" : [ "obj-48", 1 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-6", 0 ],
					"source" : [ "obj-5", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-24", 0 ],
					"source" : [ "obj-55", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-1", 0 ],
					"source" : [ "obj-61", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-47", 0 ],
					"source" : [ "obj-62", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-45", 3 ],
					"midpoints" : [ 238.5, 78.0, 225.0, 78.0, 225.0, 114.0, 207.5, 114.0 ],
					"source" : [ "obj-7", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-87", 0 ],
					"source" : [ "obj-84", 0 ]
				}

			}
, 			{
				"patchline" : 				{
					"destination" : [ "obj-7", 0 ],
					"midpoints" : [ 234.5, 273.0, 210.0, 273.0, 210.0, 195.0, 321.0, 195.0, 321.0, 42.0, 238.5, 42.0 ],
					"source" : [ "obj-87", 0 ]
				}

			}
 ],
		"parameters" : 		{
			"obj-4::obj-1::obj-1::obj-97::obj-70" : [ "hirt.val", "hirt.val", 0 ],
			"obj-4::obj-1::obj-1::obj-49" : [ "Length Mode", "Length Mode", 0 ],
			"obj-4::obj-1::obj-2::obj-81::obj-70" : [ "hirt.val[11]", "hirt.val", 0 ],
			"obj-4::obj-3::obj-59::obj-70" : [ "hirt.val[33]", "hirt.val", 0 ],
			"obj-4::obj-31::obj-56::obj-70" : [ "hirt.val[20]", "hirt.val", 0 ],
			"obj-4::obj-1::obj-1::obj-12::obj-70" : [ "hirt.val[6]", "hirt.val", 0 ],
			"obj-4::obj-8" : [ "Shape Active", "Active", 0 ],
			"obj-26" : [ "live.tab", "live.tab", 0 ],
			"obj-31" : [ "live.tab[1]", "live.tab", 0 ],
			"obj-24" : [ "live.tab[2]", "live.tab[2]", 0 ],
			"obj-4::obj-1::obj-2::obj-36::obj-70" : [ "hirt.val[8]", "hirt.val", 0 ],
			"obj-4::obj-24::obj-2::obj-49" : [ "Type", "Type", 0 ],
			"obj-4::obj-36::obj-114::obj-65" : [ "Drop B", "live.drop", 0 ],
			"obj-4::obj-3::obj-62::obj-70" : [ "hirt.val[29]", "hirt.val", 0 ],
			"obj-4::obj-24::obj-1::obj-29::obj-70" : [ "hirt.val[16]", "hirt.val", 0 ],
			"obj-4::obj-31::obj-50::obj-70" : [ "hirt.val[25]", "hirt.val", 0 ],
			"obj-17" : [ "live.text[5]", "live.text[4]", 0 ],
			"obj-4::obj-11" : [ "Modulation Active", "Active", 0 ],
			"obj-4::obj-1::obj-2::obj-100::obj-70" : [ "hirt.val[13]", "hirt.val", 0 ],
			"obj-4::obj-31::obj-55::obj-70" : [ "hirt.val[21]", "hirt.val", 0 ],
			"obj-4::obj-1::obj-1::obj-53" : [ "Direct Mode", "Direct Mode", 0 ],
			"obj-4::obj-3::obj-63::obj-70" : [ "hirt.val[30]", "hirt.val", 0 ],
			"obj-4::obj-28" : [ "PATCH/PRESS", "PATCH/PRESS", 0 ],
			"obj-4::obj-24::obj-1::obj-28::obj-70" : [ "hirt.val[17]", "hirt.val", 0 ],
			"obj-4::obj-31::obj-22::obj-70" : [ "hirt.val[26]", "hirt.val", 0 ],
			"obj-4::obj-1::obj-2::obj-101::obj-70" : [ "hirt.val[10]", "hirt.val", 0 ],
			"obj-4::obj-24::obj-2::obj-29::obj-70" : [ "hirt.val[18]", "hirt.val", 0 ],
			"obj-4::obj-31::obj-21" : [ "EQ Routing", "Active", 0 ],
			"obj-4::obj-36::obj-131::obj-10" : [ "Category Menu", "Category Menu", 0 ],
			"obj-16" : [ "live.text[4]", "live.text[4]", 0 ],
			"obj-4::obj-1::obj-1::obj-46::obj-70" : [ "hirt.val[3]", "hirt.val", 0 ],
			"obj-20" : [ "live.text[6]", "live.text", 0 ],
			"obj-4::obj-1::obj-1::obj-9" : [ "Reverse", "Reverse", 0 ],
			"obj-4::obj-108::obj-90" : [ "number", "number", 0 ],
			"obj-4::obj-31::obj-54::obj-70" : [ "hirt.val[22]", "hirt.val", 0 ],
			"obj-4::obj-1::obj-2::obj-99::obj-70" : [ "hirt.val[7]", "hirt.val", 0 ],
			"obj-4::obj-1::obj-2::obj-92::obj-70" : [ "hirt.val[15]", "hirt.val", 0 ],
			"obj-4::obj-1::obj-1::obj-48::obj-70" : [ "hirt.val[1]", "hirt.val", 0 ],
			"obj-4::obj-36::obj-131::obj-11" : [ "IR Menu", "IR Menu", 0 ],
			"obj-4::obj-3::obj-64::obj-70" : [ "hirt.val[31]", "hirt.val", 0 ],
			"obj-35" : [ "live.text[2]", "live.text[2]", 0 ],
			"obj-4::obj-31::obj-19::obj-70" : [ "hirt.val[27]", "hirt.val", 0 ],
			"obj-4::obj-24::obj-2::obj-8::obj-70" : [ "hirt.val[19]", "hirt.val", 0 ],
			"obj-4::obj-1::obj-1::obj-45::obj-70" : [ "hirt.val[4]", "hirt.val", 0 ],
			"obj-4::obj-24::obj-2::obj-25" : [ "Widen", "Widen", 0 ],
			"obj-4::obj-1::obj-2::obj-96::obj-70" : [ "hirt.val[12]", "hirt.val", 0 ],
			"obj-4::obj-36::obj-53" : [ "Mode IR", "Mode", 0 ],
			"obj-4::obj-14" : [ "Position Active", "Active", 0 ],
			"obj-4::obj-79" : [ "Offline Tabs", "Offline", 0 ],
			"obj-4::obj-31::obj-53::obj-70" : [ "hirt.val[23]", "hirt.val", 0 ],
			"obj-7" : [ "live.text", "live.text", 0 ],
			"obj-4::obj-36::obj-114::obj-35" : [ "Drop A", "live.drop", 0 ],
			"obj-4::obj-36::obj-49" : [ "Select IR", "Select", 0 ],
			"obj-4::obj-1::obj-2::obj-88::obj-70" : [ "hirt.val[9]", "hirt.val", 0 ],
			"obj-4::obj-1::obj-1::obj-47::obj-70" : [ "hirt.val[2]", "hirt.val", 0 ],
			"obj-4::obj-3::obj-65::obj-70" : [ "hirt.val[32]", "hirt.val", 0 ],
			"obj-4::obj-31::obj-17::obj-70" : [ "hirt.val[28]", "hirt.val", 0 ],
			"obj-4::obj-1::obj-1::obj-44::obj-70" : [ "hirt.val[5]", "hirt.val", 0 ],
			"obj-4::obj-10" : [ "Damp Active", "Active", 0 ],
			"obj-4::obj-1::obj-2::obj-79::obj-70" : [ "hirt.val[14]", "hirt.val", 0 ],
			"obj-4::obj-5" : [ "Realtime Tabs", "Realtime", 0 ],
			"obj-4::obj-31::obj-51::obj-70" : [ "hirt.val[24]", "hirt.val", 0 ],
			"obj-48" : [ "live.text[3]", "live.text[1]", 0 ],
			"obj-32" : [ "live.text[1]", "live.text[1]", 0 ],
			"parameterbanks" : 			{

			}
,
			"parameter_overrides" : 			{
				"obj-4::obj-1::obj-1::obj-97::obj-70" : 				{
					"parameter_invisible" : 1,
					"parameter_exponent" : 1.01,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 5,
					"parameter_initial" : 100.0,
					"parameter_range" : [ 1.0, 200.0 ]
				}
,
				"obj-4::obj-1::obj-2::obj-81::obj-70" : 				{
					"parameter_longname" : "hirt.val[11]",
					"parameter_invisible" : 1,
					"parameter_exponent" : 1.189901,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 5,
					"parameter_initial" : 100.0,
					"parameter_range" : [ 20.0, 200.0 ]
				}
,
				"obj-4::obj-3::obj-59::obj-70" : 				{
					"parameter_longname" : "hirt.val[33]",
					"parameter_exponent" : 2.0,
					"parameter_invisible" : 0,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 2,
					"parameter_initial" : 0.0,
					"parameter_range" : [ 0.0, 200.0 ]
				}
,
				"obj-4::obj-31::obj-56::obj-70" : 				{
					"parameter_longname" : "hirt.val[20]",
					"parameter_exponent" : 4.0,
					"parameter_invisible" : 0,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 3,
					"parameter_initial" : 8000.0,
					"parameter_range" : [ 10.0, 18000.0 ]
				}
,
				"obj-4::obj-1::obj-1::obj-12::obj-70" : 				{
					"parameter_longname" : "hirt.val[6]",
					"parameter_invisible" : 1,
					"parameter_exponent" : 2.5,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 2,
					"parameter_initial" : 15000.0,
					"parameter_range" : [ 100.0, 30000.0 ]
				}
,
				"obj-4::obj-1::obj-2::obj-36::obj-70" : 				{
					"parameter_longname" : "hirt.val[8]",
					"parameter_invisible" : 1,
					"parameter_exponent" : 1.189901,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 5,
					"parameter_initial" : 100.0,
					"parameter_range" : [ 20.0, 200.0 ]
				}
,
				"obj-4::obj-3::obj-62::obj-70" : 				{
					"parameter_longname" : "hirt.val[29]",
					"parameter_invisible" : 0,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 5,
					"parameter_initial" : 0.0,
					"parameter_range" : [ 0.0, 100.0 ],
					"parameter_exponent" : 1.0
				}
,
				"obj-4::obj-24::obj-1::obj-29::obj-70" : 				{
					"parameter_longname" : "hirt.val[16]",
					"parameter_invisible" : 0,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 6,
					"parameter_initial" : 0.0,
					"parameter_range" : [ -50.0, 50.0 ],
					"parameter_exponent" : 1.0
				}
,
				"obj-4::obj-31::obj-50::obj-70" : 				{
					"parameter_longname" : "hirt.val[25]",
					"parameter_exponent" : 3.0,
					"parameter_invisible" : 0,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 10,
					"parameter_initial" : 0.707107,
					"parameter_range" : [ 0.05, 18.0 ]
				}
,
				"obj-4::obj-1::obj-2::obj-100::obj-70" : 				{
					"parameter_longname" : "hirt.val[13]",
					"parameter_invisible" : 1,
					"parameter_exponent" : 4.0,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 3,
					"parameter_initial" : 1000.0,
					"parameter_range" : [ 30.0, 18000.0 ]
				}
,
				"obj-4::obj-31::obj-55::obj-70" : 				{
					"parameter_longname" : "hirt.val[21]",
					"parameter_invisible" : 0,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 4,
					"parameter_units" : " ",
					"parameter_initial" : 0.0,
					"parameter_range" : [ -18.0, 18.0 ],
					"parameter_exponent" : 1.0
				}
,
				"obj-4::obj-3::obj-63::obj-70" : 				{
					"parameter_longname" : "hirt.val[30]",
					"parameter_invisible" : 0,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 5,
					"parameter_initial" : 100.0,
					"parameter_range" : [ 0.0, 100.0 ],
					"parameter_exponent" : 1.0
				}
,
				"obj-4::obj-24::obj-1::obj-28::obj-70" : 				{
					"parameter_longname" : "hirt.val[17]",
					"parameter_invisible" : 0,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 5,
					"parameter_initial" : 0.0,
					"parameter_range" : [ -100.0, 100.0 ],
					"parameter_exponent" : 1.0
				}
,
				"obj-4::obj-31::obj-22::obj-70" : 				{
					"parameter_longname" : "hirt.val[26]",
					"parameter_exponent" : 4.0,
					"parameter_invisible" : 0,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 3,
					"parameter_initial" : 125.0,
					"parameter_range" : [ 10.0, 18000.0 ]
				}
,
				"obj-4::obj-1::obj-2::obj-101::obj-70" : 				{
					"parameter_longname" : "hirt.val[10]",
					"parameter_invisible" : 1,
					"parameter_exponent" : 4.0,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 3,
					"parameter_initial" : 8000.0,
					"parameter_range" : [ 30.0, 18000.0 ]
				}
,
				"obj-4::obj-24::obj-2::obj-29::obj-70" : 				{
					"parameter_longname" : "hirt.val[18]",
					"parameter_invisible" : 0,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 3,
					"parameter_initial" : 1.0,
					"parameter_range" : [ 0.05, 2.0 ],
					"parameter_exponent" : 1.0
				}
,
				"obj-4::obj-1::obj-1::obj-46::obj-70" : 				{
					"parameter_longname" : "hirt.val[3]",
					"parameter_invisible" : 1,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 5,
					"parameter_initial" : 100.0,
					"parameter_range" : [ 0.0, 100.0 ],
					"parameter_exponent" : 1.0
				}
,
				"obj-4::obj-31::obj-54::obj-70" : 				{
					"parameter_longname" : "hirt.val[22]",
					"parameter_exponent" : 3.0,
					"parameter_invisible" : 0,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 10,
					"parameter_initial" : 0.5,
					"parameter_range" : [ 0.05, 18.0 ]
				}
,
				"obj-4::obj-1::obj-2::obj-99::obj-70" : 				{
					"parameter_longname" : "hirt.val[7]",
					"parameter_invisible" : 1,
					"parameter_exponent" : 4.0,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 3,
					"parameter_initial" : 125.0,
					"parameter_range" : [ 30.0, 18000.0 ]
				}
,
				"obj-4::obj-1::obj-2::obj-92::obj-70" : 				{
					"parameter_longname" : "hirt.val[15]",
					"parameter_invisible" : 1,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 1,
					"parameter_initial" : 0.707107,
					"parameter_range" : [ 0.05, 2.0 ],
					"parameter_exponent" : 1.0
				}
,
				"obj-4::obj-1::obj-1::obj-48::obj-70" : 				{
					"parameter_longname" : "hirt.val[1]",
					"parameter_invisible" : 1,
					"parameter_exponent" : 1.58,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 5,
					"parameter_initial" : 100.0,
					"parameter_range" : [ 50.0, 200.0 ]
				}
,
				"obj-4::obj-3::obj-64::obj-70" : 				{
					"parameter_longname" : "hirt.val[31]",
					"parameter_invisible" : 0,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 4,
					"parameter_units" : " ",
					"parameter_initial" : 0.0,
					"parameter_range" : [ -20.0, 20.0 ],
					"parameter_exponent" : 1.0
				}
,
				"obj-4::obj-31::obj-19::obj-70" : 				{
					"parameter_longname" : "hirt.val[27]",
					"parameter_invisible" : 0,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 4,
					"parameter_units" : " ",
					"parameter_initial" : 0.0,
					"parameter_range" : [ -18.0, 18.0 ],
					"parameter_exponent" : 1.0
				}
,
				"obj-4::obj-24::obj-2::obj-8::obj-70" : 				{
					"parameter_longname" : "hirt.val[19]",
					"parameter_invisible" : 0,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 5,
					"parameter_initial" : 50.0,
					"parameter_range" : [ 0.0, 100.0 ],
					"parameter_exponent" : 1.0
				}
,
				"obj-4::obj-1::obj-1::obj-45::obj-70" : 				{
					"parameter_longname" : "hirt.val[4]",
					"parameter_invisible" : 1,
					"parameter_exponent" : 2.0,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 2,
					"parameter_initial" : 0.0,
					"parameter_range" : [ 0.0, 1000.0 ]
				}
,
				"obj-4::obj-1::obj-2::obj-96::obj-70" : 				{
					"parameter_longname" : "hirt.val[12]",
					"parameter_invisible" : 1,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 1,
					"parameter_initial" : 1.0,
					"parameter_range" : [ 0.05, 2.0 ],
					"parameter_exponent" : 1.0
				}
,
				"obj-4::obj-31::obj-53::obj-70" : 				{
					"parameter_longname" : "hirt.val[23]",
					"parameter_exponent" : 4.0,
					"parameter_invisible" : 0,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 3,
					"parameter_initial" : 1000.0,
					"parameter_range" : [ 10.0, 18000.0 ]
				}
,
				"obj-4::obj-1::obj-2::obj-88::obj-70" : 				{
					"parameter_longname" : "hirt.val[9]",
					"parameter_invisible" : 1,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 1,
					"parameter_initial" : 1.0,
					"parameter_range" : [ 0.05, 2.0 ],
					"parameter_exponent" : 1.0
				}
,
				"obj-4::obj-1::obj-1::obj-47::obj-70" : 				{
					"parameter_longname" : "hirt.val[2]",
					"parameter_invisible" : 1,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 5,
					"parameter_initial" : 100.0,
					"parameter_range" : [ 0.0, 100.0 ],
					"parameter_exponent" : 1.0
				}
,
				"obj-4::obj-3::obj-65::obj-70" : 				{
					"parameter_longname" : "hirt.val[32]",
					"parameter_invisible" : 0,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 5,
					"parameter_initial" : 50.0,
					"parameter_range" : [ 0.0, 100.0 ],
					"parameter_exponent" : 1.0
				}
,
				"obj-4::obj-31::obj-17::obj-70" : 				{
					"parameter_longname" : "hirt.val[28]",
					"parameter_exponent" : 3.0,
					"parameter_invisible" : 0,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 10,
					"parameter_initial" : 0.5,
					"parameter_range" : [ 0.05, 18.0 ]
				}
,
				"obj-4::obj-1::obj-1::obj-44::obj-70" : 				{
					"parameter_longname" : "hirt.val[5]",
					"parameter_invisible" : 1,
					"parameter_exponent" : 2.0,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 2,
					"parameter_initial" : 0.0,
					"parameter_range" : [ 0.0, 1000.0 ]
				}
,
				"obj-4::obj-1::obj-2::obj-79::obj-70" : 				{
					"parameter_longname" : "hirt.val[14]",
					"parameter_invisible" : 1,
					"parameter_exponent" : 1.189901,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 5,
					"parameter_initial" : 100.0,
					"parameter_range" : [ 20.0, 200.0 ]
				}
,
				"obj-4::obj-31::obj-51::obj-70" : 				{
					"parameter_longname" : "hirt.val[24]",
					"parameter_invisible" : 0,
					"parameter_modmode" : 0,
					"parameter_type" : 0,
					"parameter_unitstyle" : 4,
					"parameter_units" : " ",
					"parameter_initial" : 0.0,
					"parameter_range" : [ -18.0, 18.0 ],
					"parameter_exponent" : 1.0
				}

			}

		}
,
		"dependency_cache" : [ 			{
				"name" : "hirt.convolutionreverb~.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_tabs_offline.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_tab_shape.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt.dial.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt.dial.linear.only.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_tab_damp.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_interface_damp.js",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/jsui",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/jsui",
				"type" : "TEXT",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_tabs_realtime.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_tab_position.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_interface_pos.js",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/jsui",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/jsui",
				"type" : "TEXT",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_tab_modulation.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_interface_mod.js",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/jsui",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/jsui",
				"type" : "TEXT",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_eq.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_interface_eq.js",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/jsui",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/jsui",
				"type" : "TEXT",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_ir.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_file_loading.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_loading_scheme.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_file_set.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_file_check.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_base_name.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_folder.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_data_colls.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_file_ir_display.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_filter_type.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_file_picker.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_cr_info_view.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_output.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "reverb_settings.json",
				"bootpath" : "~/dev/data_bending/reaper_projects",
				"patcherrelativepath" : ".",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_convrvrb_clientlist_alias.txt",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"type" : "TEXT",
				"implicit" : 1
			}
, 			{
				"name" : "HIRT_HISSTools_Logo.png",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/misc/HIRT_image",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/misc/HIRT_image",
				"type" : "PNG",
				"implicit" : 1
			}
, 			{
				"name" : "hirt.convrvrb.realtime~.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt.convolvestereo~.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_convrvrb_rt_part1.gendsp",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/code",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/code",
				"type" : "gDSP",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_convolution_rt_library.genexpr",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/code",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/code",
				"type" : "GenX",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_eq_library.genexpr",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/code",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/code",
				"type" : "GenX",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_convrvrb_rt_part3.gendsp",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/code",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/code",
				"type" : "gDSP",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_convolution_rt_library.genexpr",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/code",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/code",
				"type" : "GenX",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_convrvrb_rt_part5.gendsp",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/code",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/code",
				"type" : "gDSP",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_convolution_rt_library.genexpr",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/code",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/code",
				"type" : "GenX",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_gain_params.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt.svfcoeff.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_zoom_factor.js",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/javascript",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/javascript",
				"type" : "TEXT",
				"implicit" : 1
			}
, 			{
				"name" : "hirt.damping.cascade.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt.buffer.filter.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_partition_late.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_partition_fix_length.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_nan_fix.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_partition_early.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_partition_copy_buffers.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_gain_and_display.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt.size.resample.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "hirt_size_resample_feed.maxpat",
				"bootpath" : "~/Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"patcherrelativepath" : "../../../Documents/Max 8/Packages/HISSTools Impulse Response Toolbox (HIRT)/patchers/HIRT_reverb/HIRT_reverb_support",
				"type" : "JSON",
				"implicit" : 1
			}
, 			{
				"name" : "lockWatch.js",
				"bootpath" : "~/dev/data_bending/reaper_projects",
				"patcherrelativepath" : ".",
				"type" : "TEXT",
				"implicit" : 1
			}
, 			{
				"name" : "spectrumdraw~.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "iraverage~.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "irdisplay~.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "irtrimnorm~.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "multiconvolve~.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "morphfilter~.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "irstats~.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "irmix~.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "ircropfade~.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "bufreverse~.mxo",
				"type" : "iLaX"
			}
, 			{
				"name" : "bufresample~.mxo",
				"type" : "iLaX"
			}
 ],
		"autosave" : 0
	}

}
