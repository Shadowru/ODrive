





# Controller.Config

## Attributes



<big><code>gain_scheduling_width - 
**<span title="C type: float, Python type: float">float32</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

_No description_</ul>

<big><code>enable_vel_limit - 
**<span title="C type: bool, Python type: bool">bool</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

_No description_</ul>

<big><code>enable_current_mode_vel_limit - 
**<span title="C type: bool, Python type: bool">bool</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

Enable velocity limit in current control mode (requires a valid velocity estimator).</ul>

<big><code>enable_gain_scheduling - 
**<span title="C type: bool, Python type: bool">bool</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

_No description_</ul>

<big><code>enable_overspeed_error - 
**<span title="C type: bool, Python type: bool">bool</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

_No description_</ul>

<big><code>control_mode - 
**[<span >ControlMode</span>](controller.controlmode.md)**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

_No description_</ul>

<big><code>input_mode - 
**[<span >InputMode</span>](controller.inputmode.md)**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

_No description_</ul>

<big><code>pos_gain - 
**<span title="C type: float, Python type: float">float32</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

_No description_</ul>

<big><code>vel_gain - 
**<span title="C type: float, Python type: float">float32</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

_No description_</ul>

<big><code>vel_integrator_gain - 
**<span title="C type: float, Python type: float">float32</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

_No description_</ul>

<big><code>vel_limit - 
**<span title="C type: float, Python type: float">float32</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>



**Unit:** counts/s

Infinity to disable.</ul>

<big><code>vel_limit_tolerance - 
**<span title="C type: float, Python type: float">float32</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

Ratio to `vel_limit`. Infinity to disable.</ul>

<big><code>vel_ramp_rate - 
**<span title="C type: float, Python type: float">float32</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

_No description_</ul>

<big><code>current_ramp_rate - 
**<span title="C type: float, Python type: float">float32</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

_No description_</ul>

<big><code>homing_speed - 
**<span title="C type: float, Python type: float">float32</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

_No description_</ul>

<big><code>inertia - 
**<span title="C type: float, Python type: float">float32</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

_No description_</ul>

<big><code>axis_to_mirror - 
**<span title="C type: uint8_t, Python type: int">uint8</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

_No description_</ul>

<big><code>mirror_ratio - 
**<span title="C type: float, Python type: float">float32</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

_No description_</ul>

<big><code>load_encoder_axis - 
**<span title="C type: uint8_t, Python type: int">uint8</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

Default depends on Axis number and is set in load_configuration()</ul>

<big><code>input_filter_bandwidth - 
**<span title="C type: float, Python type: float">float32</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

_No description_</ul>

<big><code>anticogging - **[<span >Anticogging</span>](controller.config.anticogging.md)**</code></big>

<ul>

_No description_</ul>



## Functions


This interface has no functions.
