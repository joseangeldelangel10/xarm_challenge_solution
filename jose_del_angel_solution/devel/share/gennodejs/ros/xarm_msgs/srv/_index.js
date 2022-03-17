
"use strict";

let GetErr = require('./GetErr.js')
let SetInt16 = require('./SetInt16.js')
let GetAnalogIO = require('./GetAnalogIO.js')
let SetString = require('./SetString.js')
let SetMultipleInts = require('./SetMultipleInts.js')
let SetAxis = require('./SetAxis.js')
let GripperConfig = require('./GripperConfig.js')
let PlayTraj = require('./PlayTraj.js')
let Move = require('./Move.js')
let ClearErr = require('./ClearErr.js')
let MoveVelo = require('./MoveVelo.js')
let GetDigitalIO = require('./GetDigitalIO.js')
let GripperState = require('./GripperState.js')
let SetControllerAnalogIO = require('./SetControllerAnalogIO.js')
let GetInt32 = require('./GetInt32.js')
let MoveAxisAngle = require('./MoveAxisAngle.js')
let SetDigitalIO = require('./SetDigitalIO.js')
let SetToolModbus = require('./SetToolModbus.js')
let GetControllerDigitalIO = require('./GetControllerDigitalIO.js')
let ConfigToolModbus = require('./ConfigToolModbus.js')
let GetFloat32List = require('./GetFloat32List.js')
let GripperMove = require('./GripperMove.js')
let TCPOffset = require('./TCPOffset.js')
let SetFloat32 = require('./SetFloat32.js')
let MoveVelocity = require('./MoveVelocity.js')
let SetLoad = require('./SetLoad.js')

module.exports = {
  GetErr: GetErr,
  SetInt16: SetInt16,
  GetAnalogIO: GetAnalogIO,
  SetString: SetString,
  SetMultipleInts: SetMultipleInts,
  SetAxis: SetAxis,
  GripperConfig: GripperConfig,
  PlayTraj: PlayTraj,
  Move: Move,
  ClearErr: ClearErr,
  MoveVelo: MoveVelo,
  GetDigitalIO: GetDigitalIO,
  GripperState: GripperState,
  SetControllerAnalogIO: SetControllerAnalogIO,
  GetInt32: GetInt32,
  MoveAxisAngle: MoveAxisAngle,
  SetDigitalIO: SetDigitalIO,
  SetToolModbus: SetToolModbus,
  GetControllerDigitalIO: GetControllerDigitalIO,
  ConfigToolModbus: ConfigToolModbus,
  GetFloat32List: GetFloat32List,
  GripperMove: GripperMove,
  TCPOffset: TCPOffset,
  SetFloat32: SetFloat32,
  MoveVelocity: MoveVelocity,
  SetLoad: SetLoad,
};
