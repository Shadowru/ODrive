



# Axis

## Attributes



<a name="error"></a><big><code>error - 
**[<span >Error</span>](axis.error.md)**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

_No description_</ul>

<a name="step_dir_active"></a><big><code>step_dir_active - 
**<span title="C type: bool, Python type: bool">bool</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readonly property)_</span>

<ul>

_No description_</ul>

<a name="current_state"></a><big><code>current_state - 
**[<span >AxisState</span>](axis.axisstate.md)**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readonly property)_</span>

<ul>

_No description_</ul>

<a name="requested_state"></a><big><code>requested_state - 
**[<span >AxisState</span>](axis.axisstate.md)**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

_No description_</ul>

<a name="loop_counter"></a><big><code>loop_counter - 
**<span title="C type: uint32_t, Python type: int">uint32</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readonly property)_</span>

<ul>

_No description_</ul>

<a name="lockin_state"></a><big><code>lockin_state - 
**[<span >LockinState</span>](axis.lockinstate.md)**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readonly property)_</span>

<ul>

_No description_</ul>

<a name="is_homed"></a><big><code>is_homed - 
**<span title="C type: bool, Python type: bool">bool</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

_No description_</ul>

<a name="config"></a><big><code>config - **[<span >Config</span>](axis.config.md)**</code></big>

<ul>

_No description_</ul>

<a name="motor"></a><big><code>motor - **[<span >Motor</span>](motor.md)**</code></big>

<ul>

_No description_</ul>

<a name="controller"></a><big><code>controller - **[<span >Controller</span>](controller.md)**</code></big>

<ul>

_No description_</ul>

<a name="encoder"></a><big><code>encoder - **[<span >Encoder</span>](encoder.md)**</code></big>

<ul>

_No description_</ul>

<a name="sensorless_estimator"></a><big><code>sensorless_estimator - **[<span >SensorlessEstimator</span>](sensorlessestimator.md)**</code></big>

<ul>

_No description_</ul>

<a name="trap_traj"></a><big><code>trap_traj - **[<span >TrapezoidalTrajectory</span>](trapezoidaltrajectory.md)**</code></big>

<ul>

_No description_</ul>

<a name="min_endstop"></a><big><code>min_endstop - **[<span >Endstop</span>](endstop.md)**</code></big>

<ul>

_No description_</ul>

<a name="max_endstop"></a><big><code>max_endstop - **[<span >Endstop</span>](endstop.md)**</code></big>

<ul>

_No description_</ul>



## Functions



<big><code>watchdog_feed()</code></big>

<ul>

Feed the watchdog to prevent watchdog timeouts.</ul>

<big><code>clear_errors()</code></big>

<ul>

Check the watchdog timer for expiration. Also sets the watchdog error bit if expired.</ul>

