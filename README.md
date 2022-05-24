<!--
 Copyright (c) 2022 Joseph Hale

 This Source Code Form is subject to the terms of the Mozilla Public
 License, v. 2.0. If a copy of the MPL was not distributed with this
 file, You can obtain one at http://mozilla.org/MPL/2.0/.
-->

# MultiCounter

A simple, elegant counter with support for counting multiple things at once.

## Installation

### Pip
```bash
pip install multicounter
```

### Poetry
```bash
poetry add multicounter
```

## Usage
```python
from multicounter import MultiCounter
mc = MultiCounter()

# Choose a name for your counter and start counting!
mc.foo += 1

# You can choose an initial value for a counter ...
mc.bar = 42
# ... and increment or decrement it however you like.
mc.bar -= 4

print(mc.get_counters())
# {'foo': 1, 'bar': 38}
```

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md)

## The Legal Stuff

```
`MultiCounter` by Joseph Hale is licensed under the terms of the Mozilla
Public License, v 2.0, which are available at https://mozilla.org/MPL/2.0/.

You can download the source code for `MultiCounter` for free from
https://github.com/jhale1805/multicounter.
```

### TL;DR

You can use files from this project in both open source and proprietary
applications, provided you include the above attribution. However, if
you modify any code in this project, or copy blocks of it into your own
code, you must publicly share the resulting files (note, not your whole
program) under the MPL-2.0. The best way to do this is via a Pull
Request back into this project.

If you have any other questions, you may also find Mozilla's [official
FAQ](https://www.mozilla.org/en-US/MPL/2.0/FAQ/) for the MPL-2.0
license insightful.

If you dislike this license, you can contact me about negotiating a
paid contract with different terms.

**Disclaimer:** This TL;DR is just a summary. All legal questions
regarding usage of this project must be handled according to the
official terms specified in the `LICENSE` file.

### Why the MPL-2.0 license?

I believe that an open-source software license should ensure that code
can be used everywhere.

Strict copyleft licenses, like the GPL family of licenses, fail to
fulfill that vision because they only permit code to be used in other
GPL-licensed projects. Permissive licenses, like the MIT and Apache
licenses, allow code to be used everywhere but fail to prevent
proprietary or GPL-licensed projects from limiting access to any
improvements they make.

In contrast, the MPL-2.0 license allows code to be used in any software
project, while ensuring that any improvements remain available for
everyone.
