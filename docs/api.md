#Cobra

This module contains the event class and related exceptions.

This module implements logging functionality.

##Event
=======

The event object is a callable object that allows you to delegate an event handler and listeners that are called when the event is dispatched.

###Event.set_handler(handler)
=============================

This method sets the handler function for the event. The handler function is any single callable object that is called at the event dispatch.

####Parameters

* handler - The function to be called to handle this Event on dispatch.

####Example

``` python
import events

def do_something():
    print("I do something")

event = cobra.Event()
event.add_handler(do_something)

event()
```

Output

```
I do something
```

###Event.add_listener(*args)
============================

This method adds the given arguements as 

####Parameters

* *args - Functions or callable objects to be added as listeners to this event.

##EventSystem
=============

An EventSystem is an object that allows for easier access and increased controll over a group of related cobra. An EventSystem also serves as a namespace for related cobra.

###EventSystem.get_event(*args)
===============================

This method returns the event(s) with the given names, args, in this event system.

####Parameters

* *args - Names of the events to create in this EventSystem.

####Eaxample

``` python
```

###EventSystem.get_events()

This method returns a list of all event names in this EventSystem.

####Example

``` python
import events

event_sys = cobra.EventSystem()
event_sys.add_event("test")
for e in event_sys.get_events():
    print(e)
```

Output

```
```

##EventError
============

EventError is the base exception class for all other specialized exceptions raised by this module.

##EventSystemError
==================

This is the base class of exceptions raised by the EventSystem class.