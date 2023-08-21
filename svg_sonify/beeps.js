// Simple synthetic beeps or pings
// cribbed and adapted from https://css-tricks.com/form-validation-web-audio/
//

let context = new window.AudioContext();

export
function ping(freq_hz, freq_to_hz=freq_hz,
              ramp_up_sec=0.025,
              duration_sec=0.05) {
    if (context === undefined) {
        context = new window.AudioContext();
    }
    const noise = new OscillatorNode(context,
        {frequency: freq_hz, type: "sine" });
    // We begin by quickly ramping up to freq_to_hz
    const ramp_time_target = context.currentTime + ramp_up_sec;
    noise.frequency.exponentialRampToValueAtTime(freq_to_hz, ramp_time_target);
    const gain=context.createGain();
    // We finish by diminishing to .01 volume
    gain.gain.exponentialRampToValueAtTime(0.1,
        context.currentTime + duration_sec - 0.025);
    // Not sure what this filter is for!
    const filter = new BiquadFilterNode(context,
        {
            type: "bandpass", Q: 0.01
        });
    noise.connect(filter).connect(gain).connect(context.destination);
    noise.start();
    noise.stop(context.currentTime + duration_sec);
}

// While ping is a momentary sound, sustain plays continuously until
// stopped.  It returns a noise so that it can be stopped by another
// event.
export function tone(freq_hz, freq_to_hz=freq_hz,
              ramp_up_sec=0.025) {
        if (context === undefined) {
        context = new window.AudioContext();
    }
    const noise = new OscillatorNode(context,
        {frequency: freq_hz, type: "sine" });
    // We begin by quickly ramping up to freq_to_hz
    const ramp_time_target = context.currentTime + ramp_up_sec;
    noise.frequency.exponentialRampToValueAtTime(freq_to_hz, ramp_time_target);
    const gain=context.createGain();
    // Play at 15% volume
    gain.gain.exponentialRampToValueAtTime(0.15,
        context.currentTime + 2 * ramp_up_sec);
    // Not sure what this filter is for!
    const filter = new BiquadFilterNode(context,
        {
            type: "bandpass", Q: 0.01
        });
    noise.connect(filter).connect(gain).connect(context.destination);
    return noise;
}