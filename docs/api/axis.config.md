





# Axis.Config

## Attributes



<big><code>startup_motor_calibration - 
**<span title="C type: bool, Python type: bool">bool</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

run motor calibration at startup, skip otherwise</ul>

<big><code>startup_encoder_index_search - 
**<span title="C type: bool, Python type: bool">bool</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

run encoder index search after startup, skip otherwise this only has an effect if encoder.config.use_index is also true</ul>

<big><code>startup_encoder_offset_calibration - 
**<span title="C type: bool, Python type: bool">bool</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

run encoder offset calibration after startup, skip otherwise</ul>

<big><code>startup_closed_loop_control - 
**<span title="C type: bool, Python type: bool">bool</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

enable closed loop control after calibration/startup</ul>

<big><code>startup_sensorless_control - 
**<span title="C type: bool, Python type: bool">bool</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

enable sensorless control after calibration/startup</ul>

<big><code>startup_homing - 
**<span title="C type: bool, Python type: bool">bool</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

enable homing after calibration/startup</ul>

<big><code>enable_step_dir - 
**<span title="C type: bool, Python type: bool">bool</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

Enable step/dir input after calibration. For M0 this has no effect if `enable_uart` is true.</ul>

<big><code>step_dir_always_on - 
**<span title="C type: bool, Python type: bool">bool</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

Keep step/dir enabled while the motor is disabled. This is ignored if enable_step_dir is false. This setting only takes effect on a state transition into idle or out of closed loop control.</ul>

<big><code>counts_per_step - 
**<span title="C type: float, Python type: float">float32</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

_No description_</ul>

<big><code>watchdog_timeout - 
**<span title="C type: float, Python type: float">float32</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>



**Unit:** s

0 disables watchdog</ul>

<big><code>enable_watchdog - 
**<span title="C type: bool, Python type: bool">bool</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

_No description_</ul>

<big><code>step_gpio_pin - 
**<span title="C type: uint16_t, Python type: int">uint16</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

_No description_</ul>

<big><code>dir_gpio_pin - 
**<span title="C type: uint16_t, Python type: int">uint16</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

_No description_</ul>

<big><code>calibration_lockin - **[<span >CalibrationLockin</span>](axis.config.calibrationlockin.md)**</code></big>

<ul>

_No description_</ul>

<big><code>sensorless_ramp - **[<span >LockinState</span>](axis.lockinstate.md)**</code></big>

<ul>

_No description_</ul>

<big><code>general_lockin - **[<span >LockinState</span>](axis.lockinstate.md)**</code></big>

<ul>

_No description_</ul>

<big><code>can_node_id - 
**<span title="C type: uint32_t, Python type: int">uint32</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

Both axes will have the same id to start</ul>

<big><code>can_node_id_extended - 
**<span title="C type: bool, Python type: bool">bool</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

_No description_</ul>

<big><code>can_heartbeat_rate_ms - 
**<span title="C type: uint32_t, Python type: int">uint32</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

_No description_</ul>



## Functions


This interface has no functions.
