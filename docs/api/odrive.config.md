





# Odrive.Config

## Attributes



<big><code>enable_uart - 
**<span title="C type: bool, Python type: bool">bool</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

TODO: changing this currently requires a reboot - fix this</ul>

<big><code>uart_baudrate - 
**<span title="C type: uint32_t, Python type: int">uint32</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

Defines the baudrate used on the UART interface.
Some baudrates will have a small timing error due to hardware limitations.

Here's an (incomplete) list of baudrates for ODrive v3.x:

  Configured  | Actual        | Error [%]
 -------------|---------------|-----------
  1.2 KBps    | 1.2 KBps      | 0
  2.4 KBps    | 2.4 KBps      | 0
  9.6 KBps    | 9.6 KBps      | 0
  19.2 KBps   | 19.195 KBps   | 0.02
  38.4 KBps   | 38.391 KBps   | 0.02
  57.6 KBps   | 57.613 KBps   | 0.02
  115.2 KBps  | 115.068 KBps  | 0.11
  230.4 KBps  | 230.769 KBps  | 0.16
  460.8 KBps  | 461.538 KBps  | 0.16
  921.6 KBps  | 913.043 KBps  | 0.93
  1.792 MBps  | 1.826 MBps    | 1.9
  1.8432 MBps | 1.826 MBps    | 0.93

For more information refer to Section 30.3.4 and Table 142 (the column with f_PCLK = 42 MHz) in the
[STM datasheet](https://www.st.com/content/ccc/resource/technical/document/reference_manual/3d/6d/5a/66/b4/99/40/d4/DM00031020.pdf/files/DM00031020.pdf/jcr:content/translations/en.DM00031020.pdf).
</ul>

<big><code>enable_i2c_instead_of_can - 
**<span title="C type: bool, Python type: bool">bool</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

Changing this requires a reboot.</ul>

<big><code>enable_ascii_protocol_on_usb - 
**<span title="C type: bool, Python type: bool">bool</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

_No description_</ul>

<big><code>max_regen_current - 
**<span title="C type: float, Python type: float">float32</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

_No description_</ul>

<big><code>brake_resistance - 
**<span title="C type: float, Python type: float">float32</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

Value of the brake resistor connected to the ODrive.



**Unit:** Ohm

Set to 0 to disable.</ul>

<big><code>dc_bus_undervoltage_trip_level - 
**<span title="C type: float, Python type: float">float32</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

Minimum voltage below which the motor stops operating.

**Unit:** V

</ul>

<big><code>dc_bus_overvoltage_trip_level - 
**<span title="C type: float, Python type: float">float32</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

Maximum voltage above which the motor stops operating.



**Unit:** V

This protects against cases in which the power supply fails to dissipate
the brake power if the brake resistor is disabled.
The default is 26V for the 24V board version and 52V for the 48V board version.
</ul>

<big><code>enable_dc_bus_overvoltage_ramp - 
**<span title="C type: bool, Python type: bool">bool</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="border: 1px solid; border-radius: 3px; padding: 1px 10px; color: #c35400;" title="This feature is still experimental. It may be buggy or change later. Use with caution.">Experimental</span>

<ul>

Enables the DC bus overvoltage ramp feature.

If enabled, if the measured DC voltage exceeds `dc_bus_overvoltage_ramp_start`,
the ODrive will sink more power than usual into the the brake resistor
in an attempt to bring the voltage down again.

The brake duty cycle is increased by the following amount:

 * `vbus_voltage` == `dc_bus_overvoltage_ramp_start`  =>  brake_duty_cycle += 0%
 * `vbus_voltage` == `dc_bus_overvoltage_ramp_end`  =>  brake_duty_cycle += 100%

Remarks:
 - This feature is active even when all motors are disarmed.
 - This feature is disabled if `brake_resistance` is non-positive.
</ul>

<big><code>dc_bus_overvoltage_ramp_start - 
**<span title="C type: float, Python type: float">float32</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="border: 1px solid; border-radius: 3px; padding: 1px 10px; color: #c35400;" title="This feature is still experimental. It may be buggy or change later. Use with caution.">Experimental</span>

<ul>

See `enable_dc_bus_overvoltage_ramp`.

Do not set this lower than your usual `vbus_voltage`, unless you like fried brake resistors.</ul>

<big><code>dc_bus_overvoltage_ramp_end - 
**<span title="C type: float, Python type: float">float32</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="border: 1px solid; border-radius: 3px; padding: 1px 10px; color: #c35400;" title="This feature is still experimental. It may be buggy or change later. Use with caution.">Experimental</span>

<ul>

See `enable_dc_bus_overvoltage_ramp`.

Must be larger than `dc_bus_overvoltage_ramp_start`, otherwise the ramp feature is disabled.</ul>

<big><code>dc_max_positive_current - 
**<span title="C type: float, Python type: float">float32</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

Max current the power supply can source.

**Unit:** A

</ul>

<big><code>dc_max_negative_current - 
**<span title="C type: float, Python type: float">float32</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

Max current the power supply can sink.



**Unit:** A

You most likely want a non-positive value here. Set to -INFINITY to disable.</ul>

<big><code>gpio1_pwm_mapping - **[<span >Endpoint</span>](endpoint.md)**</code></big>

<ul>

_No description_</ul>

<big><code>gpio2_pwm_mapping - **[<span >Endpoint</span>](endpoint.md)**</code></big>

<ul>

_No description_</ul>

<big><code>gpio3_pwm_mapping - **[<span >Endpoint</span>](endpoint.md)**</code></big>

<ul>

_No description_</ul>

<big><code>gpio4_pwm_mapping - **[<span >Endpoint</span>](endpoint.md)**</code></big>

<ul>

_No description_</ul>

<big><code>gpio3_analog_mapping - **[<span >Endpoint</span>](endpoint.md)**</code></big>

<ul>

_No description_</ul>

<big><code>gpio4_analog_mapping - **[<span >Endpoint</span>](endpoint.md)**</code></big>

<ul>

_No description_</ul>



## Functions


This interface has no functions.
