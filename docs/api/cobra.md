# Cobra

This module contains the event class and related exceptions.

This module implements logging functionality.

## Event

The event object is a callable object that allows you to delegate an event handler and listeners that are called when the event is dispatched.

### Event.add_listener(*args)

This method adds the given arguements as listeners.

#### Parameters

* *args - Functions or callable objects to be added as listeners to this event.

## EventError

EventError is the base exception class for all other specialized exceptions raised by this module.

## EventSystemError

This is the base class of exceptions raised by the EventSystem class.