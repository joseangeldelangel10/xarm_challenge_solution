# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from xarm_msgs/MoveVelocityRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class MoveVelocityRequest(genpy.Message):
  _md5sum = "3ff5ed26eb25726c663dac7efa05cc61"
  _type = "xarm_msgs/MoveVelocityRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# request: command specification for velocity executions.
# Units:
#	joint space/angles: radian/s
#	Cartesian space: mm/s, radian/s.

# velocities: the velocity list of the joints/tcp
#   For velo_move_joint_timed service: [joint1_velocity, ..., joint7_velocity]
#   For velo_move_line_timed service: [x_velocity, y_velocity, z_velocity, rx_velocity, ry_velocity, rz_velocity (axis-angle)]
float32[] speeds

# is_sync: this is special for velo_move_joint service, meaning whether all joints accelerate and decelerate synchronously, true for yes, false for no.
# avaiable for service velo_move_joint_timed
bool is_sync

# is_tool_coord: this is special for velo_move_line service, meaning whether motion is in tool coordinate(true) or not(false)
# avaiable for service velo_move_line_timed
bool is_tool_coord

# the maximum duration of the speed, over this time will automatically set the speed to 0
#   duration > 0: seconds, indicates the maximum number of seconds that this speed can be maintained
#   duration == 0: always effective, will not stop automativally
#   duration < 0: default value, only used to be compatible with the old protocol, equivalent to 0
# avaiable for firmware_version >= 1.8.0
float32 duration

"""
  __slots__ = ['speeds','is_sync','is_tool_coord','duration']
  _slot_types = ['float32[]','bool','bool','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       speeds,is_sync,is_tool_coord,duration

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(MoveVelocityRequest, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.speeds is None:
        self.speeds = []
      if self.is_sync is None:
        self.is_sync = False
      if self.is_tool_coord is None:
        self.is_tool_coord = False
      if self.duration is None:
        self.duration = 0.
    else:
      self.speeds = []
      self.is_sync = False
      self.is_tool_coord = False
      self.duration = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.speeds)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.speeds))
      _x = self
      buff.write(_get_struct_2Bf().pack(_x.is_sync, _x.is_tool_coord, _x.duration))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.speeds = s.unpack(str[start:end])
      _x = self
      start = end
      end += 6
      (_x.is_sync, _x.is_tool_coord, _x.duration,) = _get_struct_2Bf().unpack(str[start:end])
      self.is_sync = bool(self.is_sync)
      self.is_tool_coord = bool(self.is_tool_coord)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.speeds)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.speeds.tostring())
      _x = self
      buff.write(_get_struct_2Bf().pack(_x.is_sync, _x.is_tool_coord, _x.duration))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.speeds = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      _x = self
      start = end
      end += 6
      (_x.is_sync, _x.is_tool_coord, _x.duration,) = _get_struct_2Bf().unpack(str[start:end])
      self.is_sync = bool(self.is_sync)
      self.is_tool_coord = bool(self.is_tool_coord)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2Bf = None
def _get_struct_2Bf():
    global _struct_2Bf
    if _struct_2Bf is None:
        _struct_2Bf = struct.Struct("<2Bf")
    return _struct_2Bf
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from xarm_msgs/MoveVelocityResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class MoveVelocityResponse(genpy.Message):
  _md5sum = "76c68a2c5e109f4d6a4dc1cfc355f405"
  _type = "xarm_msgs/MoveVelocityResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """
# response: 
#	ret is 0 for successful execution and others for errors or warnings occured
#	message is a string returned by function, indicating execution status.

int16 ret

string message
"""
  __slots__ = ['ret','message']
  _slot_types = ['int16','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       ret,message

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(MoveVelocityResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.ret is None:
        self.ret = 0
      if self.message is None:
        self.message = ''
    else:
      self.ret = 0
      self.message = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.ret
      buff.write(_get_struct_h().pack(_x))
      _x = self.message
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 2
      (self.ret,) = _get_struct_h().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.message = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.message = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.ret
      buff.write(_get_struct_h().pack(_x))
      _x = self.message
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 2
      (self.ret,) = _get_struct_h().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.message = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.message = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_h = None
def _get_struct_h():
    global _struct_h
    if _struct_h is None:
        _struct_h = struct.Struct("<h")
    return _struct_h
class MoveVelocity(object):
  _type          = 'xarm_msgs/MoveVelocity'
  _md5sum = 'ba6e5e4cb25baf01712a273c753becc6'
  _request_class  = MoveVelocityRequest
  _response_class = MoveVelocityResponse
