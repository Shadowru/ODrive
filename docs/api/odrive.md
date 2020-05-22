





# Odrive

## Attributes



<big><code>vbus_voltage: 
**<span title="C type: float, Python type: float">float32</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readonly property)_</span>

<ul>

Voltage on the DC bus as measured by the ODrive.

**Unit:** V

</ul>

<big><code>ibus: 
**<span title="C type: float, Python type: float">float32</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readonly property)_</span>

<ul>

Current on the DC bus as calculated by the ODrive.



**Unit:** A

A positive value means that the ODrive is consuming power from the power supply,
a negative value means that the ODrive is sourcing power to the power supply.

This value is equal to the sum of the motor currents and the brake resistor currents.
The motor currents are measured, the brake resistor current is calculated based on
`config.brake_resistance`.
</ul>

<big><code>serial_number: 
**<span title="C type: uint64_t, Python type: int">uint64</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readonly property)_</span>

<ul>

_No description_</ul>

<big><code>hw_version_major: 
**<span title="C type: uint8_t, Python type: int">uint8</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readonly property)_</span>

<ul>

_No description_</ul>

<big><code>hw_version_minor: 
**<span title="C type: uint8_t, Python type: int">uint8</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readonly property)_</span>

<ul>

_No description_</ul>

<big><code>hw_version_variant: 
**<span title="C type: uint8_t, Python type: int">uint8</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readonly property)_</span>

<ul>

_No description_</ul>

<big><code>fw_version_major: 
**<span title="C type: uint8_t, Python type: int">uint8</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readonly property)_</span>

<ul>

_No description_</ul>

<big><code>fw_version_minor: 
**<span title="C type: uint8_t, Python type: int">uint8</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readonly property)_</span>

<ul>

_No description_</ul>

<big><code>fw_version_revision: 
**<span title="C type: uint8_t, Python type: int">uint8</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readonly property)_</span>

<ul>

_No description_</ul>

<big><code>fw_version_unreleased: 
**<span title="C type: uint8_t, Python type: int">uint8</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readonly property)_</span>

<ul>

0 for official releases, 1 otherwise</ul>

<big><code>brake_resistor_armed: 
**<span title="C type: bool, Python type: bool">bool</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readonly property)_</span>

<ul>

_No description_</ul>

<big><code>brake_resistor_saturated: 
**<span title="C type: bool, Python type: bool">bool</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

_No description_</ul>

<big><code>system_stats: **[<span >SystemStats</span>](odrive.systemstats.md)**</code></big>

<ul>

_No description_</ul>

<big><code>config: **[<span >Config</span>](odrive.config.md)**</code></big>

<ul>

_No description_</ul>

<big><code>user_config_loaded: 
**<span title="C type: bool, Python type: bool">bool</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readonly property)_</span>

<ul>

_No description_</ul>

<big><code>axis0: **[<span >Axis</span>](axis.md)**</code></big>

<ul>

_No description_</ul>

<big><code>axis1: **[<span >Axis</span>](axis.md)**</code></big>

<ul>

_No description_</ul>

<big><code>can: **[<span >Can</span>](odrive.can.md)**</code></big>

<ul>

_No description_</ul>

<big><code>test_property: 
**<span title="C type: uint32_t, Python type: int">uint32</span>**</code></big>&nbsp;&nbsp;&nbsp;&nbsp;<span style="font-size: small;">_(readwrite property)_</span>

<ul>

_No description_</ul>



## Functions



<big><code>test_function(delta: 
**<span title="C type: int32_t, Python type: int">int32</span>**) -> cnt: 
**<span title="C type: int32_t, Python type: int">int32</span>**</code></big>

<ul>

_No description_</ul>

<big><code>get_oscilloscope_val(index: 
**<span title="C type: uint32_t, Python type: int">uint32</span>**) -> val: 
**<span title="C type: float, Python type: float">float32</span>**</code></big>

<ul>

_No description_</ul>

<big><code>get_adc_voltage(gpio: 
**<span title="C type: uint32_t, Python type: int">uint32</span>**) -> voltage: 
**<span title="C type: float, Python type: float">float32</span>**</code></big>

<ul>

_No description_</ul>

<big><code>save_configuration()</code></big>

<ul>

_No description_</ul>

<big><code>erase_configuration()</code></big>

<ul>

_No description_</ul>

<big><code>reboot()</code></big>

<ul>

_No description_</ul>

<big><code>enter_dfu_mode()</code></big>

<ul>

_No description_</ul>

