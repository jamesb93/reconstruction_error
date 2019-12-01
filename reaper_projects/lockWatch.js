var polling = new Task(state);
var actual_state;

function state() {
	actual_state = this.patcher.getattr("locked");
	outlet(0, actual_state);
}
function watch() {
	    polling.interval = 500;
	    polling.repeat();
}