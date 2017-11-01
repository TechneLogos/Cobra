# Cobra

This module contains the event class and related exceptions.

This module implements logging functionality.

## Event

The event object is a callable object that allows you to delegate an event handler and listeners that are called when the event is dispatched.

### Event.add_listener(*args)

This method adds the given arguements as listeners.

#### Parameters

* *args - Functions or callable objects to be added as listeners to this event.

## EventSystem

An EventSystem is an object that allows for easier access and increased controll over a group of related cobra. An EventSystem also serves as a namespace for related cobra.

### EventSystem.get_event(name)

This method returns the event(s) with the given names, args, in this event system.

#### Parameters

* name - Name of the event to find.

#### Example

``` python
```

### EventSystem.get_event\_names()

This method returns a list of all event names in this EventSystem.

#### Example

``` python
import events

event_system = cobra.EventSystem()
event_system.get_event("test").add_listener(some_function)
for e in event_system.get_event_names():
    print(str(e))
```

Output

```
test
```

## EventError

EventError is the base exception class for all other specialized exceptions raised by this module.

## EventSystemError

This is the base class of exceptions raised by the EventSystem class.