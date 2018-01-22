# ScienceLogic
A Python library for ScienceLogic EM7 API I created during my 17 summer intern, supporting suspension and device ID lookup.

## Usage

Create ScienceLogic instance:
```python

import ScienceLogic

sl = ScienceLogic('https://', 'account', 'password')

```

Look for Deivce ID:
```python

sl.get_id('device_name')

```

Disable/Enable monitoring on devices:
```python

sl.disable_monitoring('device_id'))

sl.enable_monitoring('device_id'))

```
