
"use strict";

let SetControllerAnalogIO = require('./SetControllerAnalogIO.js')
let SetMultipleInts = require('./SetMultipleInts.js')
let GetErr = require('./GetErr.js')
let SetToolModbus = require('./SetToolModbus.js')
let GetInt32 = require('./GetInt32.js')
let SetDigitalIO = require('./SetDigitalIO.js')
let MoveAxisAngle = require('./MoveAxisAngle.js')
let GetDigitalIO = require('./GetDigitalIO.js')
let GetFloat32List = require('./GetFloat32List.js')
let SetFloat32 = require('./SetFloat32.js')
let SetAxis = require('./SetAxis.js')
let SetLoad = require('./SetLoad.js')
let GripperState = require('./GripperState.js')
let SetInt16 = require('./SetInt16.js')
let ConfigToolModbus = require('./ConfigToolModbus.js')
let GripperMove = require('./GripperMove.js')
let MoveVelocity = require('./MoveVelocity.js')
let GripperConfig = require('./GripperConfig.js')
let Move = require('./Move.js')
let GetControllerDigitalIO = require('./GetControllerDigitalIO.js')
let GetAnalogIO = require('./GetAnalogIO.js')
let TCPOffset = require('./TCPOffset.js')
let PlayTraj = require('./PlayTraj.js')
let MoveVelo = require('./MoveVelo.js')
let ClearErr = require('./ClearErr.js')
let SetString = require('./SetString.js')

module.exports = {
  SetControllerAnalogIO: SetControllerAnalogIO,
  SetMultipleInts: SetMultipleInts,
  GetErr: GetErr,
  SetToolModbus: SetToolModbus,
  GetInt32: GetInt32,
  SetDigitalIO: SetDigitalIO,
  MoveAxisAngle: MoveAxisAngle,
  GetDigitalIO: GetDigitalIO,
  GetFloat32List: GetFloat32List,
  SetFloat32: SetFloat32,
  SetAxis: SetAxis,
  SetLoad: SetLoad,
  GripperState: GripperState,
  SetInt16: SetInt16,
  ConfigToolModbus: ConfigToolModbus,
  GripperMove: GripperMove,
  MoveVelocity: MoveVelocity,
  GripperConfig: GripperConfig,
  Move: Move,
  GetControllerDigitalIO: GetControllerDigitalIO,
  GetAnalogIO: GetAnalogIO,
  TCPOffset: TCPOffset,
  PlayTraj: PlayTraj,
  MoveVelo: MoveVelo,
  ClearErr: ClearErr,
  SetString: SetString,
};
