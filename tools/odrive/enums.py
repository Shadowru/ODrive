
# TODO: This file is dangerous because the enums could potentially change between API versions. Should transmit as part of the JSON.

# Odrive.Can.Protocol
PROTOCOL_SIMPLE                          = 0

# Axis.AxisState
AXIS_STATE_UNDEFINED                     = 0
AXIS_STATE_IDLE                          = 1
AXIS_STATE_STARTUP_SEQUENCE              = 2
AXIS_STATE_FULL_CALIBRATION_SEQUENCE     = 3
AXIS_STATE_MOTOR_CALIBRATION             = 4
AXIS_STATE_SENSORLESS_CONTROL            = 5
AXIS_STATE_ENCODER_INDEX_SEARCH          = 6
AXIS_STATE_ENCODER_OFFSET_CALIBRATION    = 7
AXIS_STATE_CLOSED_LOOP_CONTROL           = 8
AXIS_STATE_LOCKIN_SPIN                   = 9
AXIS_STATE_ENCODER_DIR_FIND              = 10
AXIS_STATE_HOMING                        = 11

# Encoder.Mode
ENCODER_MODE_INCREMENTAL                 = 0
ENCODER_MODE_HALL                        = 1
ENCODER_MODE_SINCOS                      = 2
ENCODER_MODE_SPI_ABS_CUI                 = 256
ENCODER_MODE_SPI_ABS_AMS                 = 257
ENCODER_MODE_SPI_ABS_AEAT                = 258

# Controller.ControlMode
CONTROL_MODE_VOLTAGE_CONTROL             = 0
CONTROL_MODE_CURRENT_CONTROL             = 1
CONTROL_MODE_VELOCITY_CONTROL            = 2
CONTROL_MODE_POSITION_CONTROL            = 3

# Controller.InputMode
INPUT_MODE_INACTIVE                      = 0
INPUT_MODE_PASSTHROUGH                   = 1
INPUT_MODE_VEL_RAMP                      = 2
INPUT_MODE_POS_FILTER                    = 3
INPUT_MODE_MIX_CHANNELS                  = 4
INPUT_MODE_TRAP_TRAJ                     = 5
INPUT_MODE_CURRENT_RAMP                  = 6
INPUT_MODE_MIRROR                        = 7

# Motor.MotorType
MOTOR_TYPE_HIGH_CURRENT                  = 0
MOTOR_TYPE_GIMBAL                        = 2
MOTOR_TYPE_ACIM                          = 3

# Odrive.Can.Error
CAN_ERROR_NONE                           = 0x00000000
CAN_ERROR_DUPLICATE_CAN_IDS              = 0x00000001

# Axis.Error
AXIS_ERROR_NONE                          = 0x00000000
AXIS_ERROR_INVALID_STATE                 = 0x00000001
AXIS_ERROR_DC_BUS_UNDER_VOLTAGE          = 0x00000002
AXIS_ERROR_DC_BUS_OVER_VOLTAGE           = 0x00000004
AXIS_ERROR_CURRENT_MEASUREMENT_TIMEOUT   = 0x00000008
AXIS_ERROR_BRAKE_RESISTOR_DISARMED       = 0x00000010
AXIS_ERROR_MOTOR_DISARMED                = 0x00000020
AXIS_ERROR_MOTOR_FAILED                  = 0x00000040
AXIS_ERROR_SENSORLESS_ESTIMATOR_FAILED   = 0x00000080
AXIS_ERROR_ENCODER_FAILED                = 0x00000100
AXIS_ERROR_CONTROLLER_FAILED             = 0x00000200
AXIS_ERROR_POS_CTRL_DURING_SENSORLESS    = 0x00000400
AXIS_ERROR_WATCHDOG_TIMER_EXPIRED        = 0x00000800
AXIS_ERROR_MIN_ENDSTOP_PRESSED           = 0x00001000
AXIS_ERROR_MAX_ENDSTOP_PRESSED           = 0x00002000
AXIS_ERROR_ESTOP_REQUESTED               = 0x00004000
AXIS_ERROR_HOMING_WITHOUT_ENDSTOP        = 0x00020000

# Axis.LockinState
LOCKIN_STATE_INACTIVE                    = 0
LOCKIN_STATE_RAMP                        = 1
LOCKIN_STATE_ACCELERATE                  = 2
LOCKIN_STATE_CONST_VEL                   = 3

# Motor.Error
MOTOR_ERROR_NONE                         = 0x00000000
MOTOR_ERROR_PHASE_RESISTANCE_OUT_OF_RANGE = 0x00000001
MOTOR_ERROR_PHASE_INDUCTANCE_OUT_OF_RANGE = 0x00000002
MOTOR_ERROR_ADC_FAILED                   = 0x00000004
MOTOR_ERROR_DRV_FAULT                    = 0x00000008
MOTOR_ERROR_CONTROL_DEADLINE_MISSED      = 0x00000010
MOTOR_ERROR_NOT_IMPLEMENTED_MOTOR_TYPE   = 0x00000020
MOTOR_ERROR_BRAKE_CURRENT_OUT_OF_RANGE   = 0x00000040
MOTOR_ERROR_MODULATION_MAGNITUDE         = 0x00000080
MOTOR_ERROR_BRAKE_DEADTIME_VIOLATION     = 0x00000100
MOTOR_ERROR_UNEXPECTED_TIMER_CALLBACK    = 0x00000200
MOTOR_ERROR_CURRENT_SENSE_SATURATION     = 0x00000400
MOTOR_ERROR_INVERTER_OVER_TEMP           = 0x00000800
MOTOR_ERROR_CURRENT_LIMIT_VIOLATION      = 0x00001000
MOTOR_ERROR_BRAKE_DUTY_CYCLE_NAN         = 0x00002000
MOTOR_ERROR_DC_BUS_OVER_REGEN_CURRENT    = 0x00004000
MOTOR_ERROR_DC_BUS_OVER_CURRENT          = 0x00008000

# Motor.ArmedState
ARMED_STATE_DISARMED                     = 0
ARMED_STATE_WAITING_FOR_TIMINGS          = 1
ARMED_STATE_WAITING_FOR_UPDATE           = 2
ARMED_STATE_ARMED                        = 3

# Motor.GateDriver.DrvFault
DRV_FAULT_NO_FAULT                       = 0x00000000
DRV_FAULT_FET_LOW_C_OVERCURRENT          = 0x00000001
DRV_FAULT_FET_HIGH_C_OVERCURRENT         = 0x00000002
DRV_FAULT_FET_LOW_B_OVERCURRENT          = 0x00000004
DRV_FAULT_FET_HIGH_B_OVERCURRENT         = 0x00000008
DRV_FAULT_FET_LOW_A_OVERCURRENT          = 0x00000010
DRV_FAULT_FET_HIGH_A_OVERCURRENT         = 0x00000020
DRV_FAULT_OVERTEMPERATURE_WARNING        = 0x00000040
DRV_FAULT_OVERTEMPERATURE_SHUTDOWN       = 0x00000080
DRV_FAULT_P_VDD_UNDERVOLTAGE             = 0x00000100
DRV_FAULT_G_VDD_UNDERVOLTAGE             = 0x00000200
DRV_FAULT_G_VDD_OVERVOLTAGE              = 0x00000400

# Controller.Error
CONTROLLER_ERROR_NONE                    = 0x00000000
CONTROLLER_ERROR_OVERSPEED               = 0x00000001
CONTROLLER_ERROR_INVALID_INPUT_MODE      = 0x00000002
CONTROLLER_ERROR_UNSTABLE_GAIN           = 0x00000004
CONTROLLER_ERROR_INVALID_MIRROR_AXIS     = 0x00000008
CONTROLLER_ERROR_INVALID_LOAD_ENCODER    = 0x00000010
CONTROLLER_ERROR_INVALID_ESTIMATE        = 0x00000020

# Encoder.Error
ENCODER_ERROR_NONE                       = 0x00000000
ENCODER_ERROR_UNSTABLE_GAIN              = 0x00000001
ENCODER_ERROR_CPR_POLEPAIRS_MISMATCH     = 0x00000002
ENCODER_ERROR_NO_RESPONSE                = 0x00000004
ENCODER_ERROR_UNSUPPORTED_ENCODER_MODE   = 0x00000008
ENCODER_ERROR_ILLEGAL_HALL_STATE         = 0x00000010
ENCODER_ERROR_INDEX_NOT_FOUND_YET        = 0x00000020
ENCODER_ERROR_ABS_SPI_TIMEOUT            = 0x00000040
ENCODER_ERROR_ABS_SPI_COM_FAIL           = 0x00000080
ENCODER_ERROR_ABS_SPI_NOT_READY          = 0x00000100

# SensorlessEstimator.Error
SENSORLESS_ESTIMATOR_ERROR_NONE          = 0x00000000
SENSORLESS_ESTIMATOR_ERROR_UNSTABLE_GAIN = 0x00000001
