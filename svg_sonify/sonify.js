// Script attaches sounds to html or svg elements by selector
//
import {ping, tone} from "./beeps.js"

// Sonify a single element.  Options can include
// pitch or frequency.

export function ping_in_out(selector,
                            {
                           freq_hz = 200,
                           freq_to_hz = freq_hz,
                           ramp_up_sec = 0.025,
                           duration_sec = 0.05
                       } = {}) {
    const elements = document.querySelectorAll(selector);
    elements.forEach((element) => {
        element.addEventListener("pointerenter",
            () => {
                ping(freq_hz, freq_to_hz, ramp_up_sec, duration_sec);
            })
        // Uniform tick for leaving shape
        element.addEventListener("pointerleave",
            () => {
                ping(400, 200, 0.05)
            });

    });
}

// Play a tone while over a graphic
export function tone_over(selector,
                            {
                           freq_hz = 200,
                           freq_to_hz = freq_hz,
                           ramp_up_sec = 0.025
                       } = {}) {
    console.log("Selector is " + selector);
    console.log("Options are " + {freq_hz, freq_to_hz, ramp_up_sec});
    const elements = document.querySelectorAll(selector);
    elements.forEach((element) => {
        element.addEventListener("pointerenter",
            () => {
                const el = element;
                const drone = tone(freq_hz, freq_to_hz, ramp_up_sec);
                drone.start();
                el.addEventListener("pointerleave",
                    () => { drone.stop(); },
                    {once: true});
            });
    })
}
