#!/usr/bin/env -P /usr/bin:/usr/local/bin python3 -B
# coding: utf-8

#
#  Whiteboard.py
#  Whiteboard
#  Created by Ingenuity i/o on 2023/11/19
#
# "no description"
#

import ingescape as igs

def title_input_callback(agent, iop_type, name, value_type, value, my_data):
    agent_object = my_data
    assert isinstance(agent_object, Whiteboard)
    agent_object.titleI = value
    pass
    # add code here if needed

def backgroundColor_input_callback(agent, iop_type, name, value_type, value, my_data):
    agent_object = my_data
    assert isinstance(agent_object, Whiteboard)
    agent_object.backgroundColorI = value
    pass
    # add code here if needed

def chatMessage_input_callback(agent, iop_type, name, value_type, value, my_data):
    agent_object = my_data
    assert isinstance(agent_object, Whiteboard)
    agent_object.chatMessageI = value
    pass
    # add code here if needed

def clear_input_callback(agent, iop_type, name, value_type, value, my_data):
    pass
    # add code here if needed

def ui_command_input_callback(agent, iop_type, name, value_type, value, my_data):
    agent_object = my_data
    assert isinstance(agent_object, Whiteboard)
    agent_object.ui_commandI = value
    pass
    # add code here if needed


# services
def chat_callback(agent, sender_agent_name, sender_agent_uuid, service_name, tuple_args, token, my_data):
    agent_object = my_data
    assert isinstance(agent_object, Whiteboard)
    message = tuple_args[0]
    agent_object.chat(sender_agent_name, sender_agent_uuid, message)

def snapshot_callback(agent, sender_agent_name, sender_agent_uuid, service_name, tuple_args, token, my_data):
    agent_object = my_data
    assert isinstance(agent_object, Whiteboard)
    agent_object.snapshot(sender_agent_name, sender_agent_uuid)

def clear_callback(agent, sender_agent_name, sender_agent_uuid, service_name, tuple_args, token, my_data):
    agent_object = my_data
    assert isinstance(agent_object, Whiteboard)
    agent_object.clear(sender_agent_name, sender_agent_uuid)

def addShape_callback(agent, sender_agent_name, sender_agent_uuid, service_name, tuple_args, token, my_data):
    agent_object = my_data
    assert isinstance(agent_object, Whiteboard)
    type = tuple_args[0]
    x = tuple_args[1]
    y = tuple_args[2]
    width = tuple_args[3]
    height = tuple_args[4]
    fill = tuple_args[5]
    stroke = tuple_args[6]
    strokeWidth = tuple_args[7]
    agent_object.addShape(sender_agent_name, sender_agent_uuid, type, x, y, width, height, fill, stroke, strokeWidth)

def addText_callback(agent, sender_agent_name, sender_agent_uuid, service_name, tuple_args, token, my_data):
    agent_object = my_data
    assert isinstance(agent_object, Whiteboard)
    text = tuple_args[0]
    x = tuple_args[1]
    y = tuple_args[2]
    color = tuple_args[3]
    agent_object.addText(sender_agent_name, sender_agent_uuid, text, x, y, color)

def addImage_callback(agent, sender_agent_name, sender_agent_uuid, service_name, tuple_args, token, my_data):
    agent_object = my_data
    assert isinstance(agent_object, Whiteboard)
    base64 = tuple_args[0]
    x = tuple_args[1]
    y = tuple_args[2]
    width = tuple_args[3]
    height = tuple_args[4]
    agent_object.addImage(sender_agent_name, sender_agent_uuid, base64, x, y, width, height)

def addImageFromUrl_callback(agent, sender_agent_name, sender_agent_uuid, service_name, tuple_args, token, my_data):
    agent_object = my_data
    assert isinstance(agent_object, Whiteboard)
    url = tuple_args[0]
    x = tuple_args[1]
    y = tuple_args[2]
    agent_object.addImageFromUrl(sender_agent_name, sender_agent_uuid, url, x, y)

def remove_callback(agent, sender_agent_name, sender_agent_uuid, service_name, tuple_args, token, my_data):
    agent_object = my_data
    assert isinstance(agent_object, Whiteboard)
    elementId = tuple_args[0]
    agent_object.remove(sender_agent_name, sender_agent_uuid, elementId)

def translate_callback(agent, sender_agent_name, sender_agent_uuid, service_name, tuple_args, token, my_data):
    agent_object = my_data
    assert isinstance(agent_object, Whiteboard)
    elementId = tuple_args[0]
    dx = tuple_args[1]
    dy = tuple_args[2]
    agent_object.translate(sender_agent_name, sender_agent_uuid, elementId, dx, dy)

def moveTo_callback(agent, sender_agent_name, sender_agent_uuid, service_name, tuple_args, token, my_data):
    agent_object = my_data
    assert isinstance(agent_object, Whiteboard)
    elementId = tuple_args[0]
    x = tuple_args[1]
    y = tuple_args[2]
    agent_object.moveTo(sender_agent_name, sender_agent_uuid, elementId, x, y)

def setStringProperty_callback(agent, sender_agent_name, sender_agent_uuid, service_name, tuple_args, token, my_data):
    agent_object = my_data
    assert isinstance(agent_object, Whiteboard)
    elementId = tuple_args[0]
    property = tuple_args[1]
    value = tuple_args[2]
    agent_object.setStringProperty(sender_agent_name, sender_agent_uuid, elementId, property, value)

def setDoubleProperty_callback(agent, sender_agent_name, sender_agent_uuid, service_name, tuple_args, token, my_data):
    agent_object = my_data
    assert isinstance(agent_object, Whiteboard)
    elementId = tuple_args[0]
    property = tuple_args[1]
    value = tuple_args[2]
    agent_object.setDoubleProperty(sender_agent_name, sender_agent_uuid, elementId, property, value)

def getElementIds_callback(agent, sender_agent_name, sender_agent_uuid, service_name, tuple_args, token, my_data):
    agent_object = my_data
    assert isinstance(agent_object, Whiteboard)
    agent_object.getElementIds(sender_agent_name, sender_agent_uuid)

def getElements_callback(agent, sender_agent_name, sender_agent_uuid, service_name, tuple_args, token, my_data):
    agent_object = my_data
    assert isinstance(agent_object, Whiteboard)
    agent_object.getElements(sender_agent_name, sender_agent_uuid)




class Whiteboard(igs.Agent):
    def __init__(self, activated = True):
        super().__init__("Whiteboard", activated)

        self.titleI = None
        self.backgroundColorI = None
        self.chatMessageI = None
        self.ui_commandI = None

        # outputs
        self._lastChatMessageO = None
        self._lastActionO = None
        self._ui_errorO = None

        self.input_create("title", igs.STRING_T, None)
        self.input_create("backgroundColor", igs.STRING_T, None)
        self.input_create("chatMessage", igs.STRING_T, None)
        self.input_create("clear", igs.IMPULSION_T, None)
        self.input_create("ui_command", igs.STRING_T, None)

        self.observe_input("title", title_input_callback, self)
        self.observe_input("backgroundColor", backgroundColor_input_callback, self)
        self.observe_input("chatMessage", chatMessage_input_callback, self)
        self.observe_input("clear", clear_input_callback, self)
        self.observe_input("ui_command", ui_command_input_callback, self)

        self.output_create("lastChatMessage", igs.STRING_T, None)
        self.output_create("lastAction", igs.STRING_T, None)
        self.output_create("ui_error", igs.STRING_T, None)

        self.service_init("chat", chat_callback, self)
        self.service_arg_add("chat", "message", igs.STRING_T)

        self.service_init("snapshot", snapshot_callback, self)

        self.service_init("clear", clear_callback, self)

        self.service_init("addShape", addShape_callback, self)
        self.service_arg_add("addShape", "type", igs.STRING_T)
        self.service_arg_add("addShape", "x", igs.DOUBLE_T)
        self.service_arg_add("addShape", "y", igs.DOUBLE_T)
        self.service_arg_add("addShape", "width", igs.DOUBLE_T)
        self.service_arg_add("addShape", "height", igs.DOUBLE_T)
        self.service_arg_add("addShape", "fill", igs.STRING_T)
        self.service_arg_add("addShape", "stroke", igs.STRING_T)
        self.service_arg_add("addShape", "strokeWidth", igs.DOUBLE_T)

        self.service_init("addText", addText_callback, self)
        self.service_arg_add("addText", "text", igs.STRING_T)
        self.service_arg_add("addText", "x", igs.DOUBLE_T)
        self.service_arg_add("addText", "y", igs.DOUBLE_T)
        self.service_arg_add("addText", "color", igs.STRING_T)

        self.service_init("set_background", addText_callback, self)
        self.service_arg_add("set_background", "tuple_rgb", igs.STRING_T)

        self.service_init("addImage", addImage_callback, self)
        self.service_arg_add("addImage", "base64", igs.DATA_T)
        self.service_arg_add("addImage", "x", igs.DOUBLE_T)
        self.service_arg_add("addImage", "y", igs.DOUBLE_T)
        self.service_arg_add("addImage", "width", igs.DOUBLE_T)
        self.service_arg_add("addImage", "height", igs.DOUBLE_T)

        self.service_init("addImageFromUrl", addImageFromUrl_callback, self)
        self.service_arg_add("addImageFromUrl", "url", igs.STRING_T)
        self.service_arg_add("addImageFromUrl", "x", igs.DOUBLE_T)
        self.service_arg_add("addImageFromUrl", "y", igs.DOUBLE_T)

        self.service_init("remove", remove_callback, self)
        self.service_arg_add("remove", "elementId", igs.INTEGER_T)

        self.service_init("translate", translate_callback, self)
        self.service_arg_add("translate", "elementId", igs.INTEGER_T)
        self.service_arg_add("translate", "dx", igs.DOUBLE_T)
        self.service_arg_add("translate", "dy", igs.DOUBLE_T)

        self.service_init("moveTo", moveTo_callback, self)
        self.service_arg_add("moveTo", "elementId", igs.INTEGER_T)
        self.service_arg_add("moveTo", "x", igs.DOUBLE_T)
        self.service_arg_add("moveTo", "y", igs.DOUBLE_T)

        self.service_init("setStringProperty", setStringProperty_callback, self)
        self.service_arg_add("setStringProperty", "elementId", igs.INTEGER_T)
        self.service_arg_add("setStringProperty", "property", igs.STRING_T)
        self.service_arg_add("setStringProperty", "value", igs.STRING_T)

        self.service_init("setDoubleProperty", setDoubleProperty_callback, self)
        self.service_arg_add("setDoubleProperty", "elementId", igs.INTEGER_T)
        self.service_arg_add("setDoubleProperty", "property", igs.STRING_T)
        self.service_arg_add("setDoubleProperty", "value", igs.DOUBLE_T)

        self.service_init("getElementIds", getElementIds_callback, self)

        self.service_init("getElements", getElements_callback, self)


    @property
    def lastChatMessageO(self):
        return self._lastChatMessageO

    @lastChatMessageO.setter
    def lastChatMessageO(self, value):
        self._lastChatMessageO = value
        if self._lastChatMessageO is not None:
            self.output_set_string("lastChatMessage", self._lastChatMessageO)
    @property
    def lastActionO(self):
        return self._lastActionO

    @lastActionO.setter
    def lastActionO(self, value):
        self._lastActionO = value
        if self._lastActionO is not None:
            self.output_set_string("lastAction", self._lastActionO)
    @property
    def ui_errorO(self):
        return self._ui_errorO

    @ui_errorO.setter
    def ui_errorO(self, value):
        self._ui_errorO = value
        if self._ui_errorO is not None:
            self.output_set_string("ui_error", self._ui_errorO)

    # services
    def chat(self, sender_agent_name, sender_agent_uuid, message):
        pass
        # add code here if needed

    def snapshot(self, sender_agent_name, sender_agent_uuid):
        pass
        # add code here if needed

    def clear(self, sender_agent_name, sender_agent_uuid):
        pass
        # add code here if needed

    def addShape(self, sender_agent_name, sender_agent_uuid, type, x, y, width, height, fill, stroke, strokeWidth):
        pass
        # add code here if needed

    def addText(self, sender_agent_name, sender_agent_uuid, text, x, y, color):
        pass
        # add code here if needed

    def addImage(self, sender_agent_name, sender_agent_uuid, base64, x, y, width, height):
        pass
        # add code here if needed

    def addImageFromUrl(self, sender_agent_name, sender_agent_uuid, url, x, y):
        pass
        # add code here if needed

    def remove(self, sender_agent_name, sender_agent_uuid, elementId):
        pass
        # add code here if needed

    def translate(self, sender_agent_name, sender_agent_uuid, elementId, dx, dy):
        pass
        # add code here if needed

    def moveTo(self, sender_agent_name, sender_agent_uuid, elementId, x, y):
        pass
        # add code here if needed

    def setStringProperty(self, sender_agent_name, sender_agent_uuid, elementId, property, value):
        pass
        # add code here if needed

    def setDoubleProperty(self, sender_agent_name, sender_agent_uuid, elementId, property, value):
        pass
        # add code here if needed

    def getElementIds(self, sender_agent_name, sender_agent_uuid):
        pass
        # add code here if needed

    def getElements(self, sender_agent_name, sender_agent_uuid):
        pass
        # add code here if needed


