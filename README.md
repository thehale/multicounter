<!--
 Copyright (c) 2022 Joseph Hale

 This Source Code Form is subject to the terms of the Mozilla Public
 License, v. 2.0. If a copy of the MPL was not distributed with this
 file, You can obtain one at http://mozilla.org/MPL/2.0/.
-->

# MultiCounter

A simple, elegant counter with support for counting multiple things at once.

<!-- BADGES -->
[![](https://badgen.net/github/license/thehale/multicounter)](https://github.com/thehale/multicounter/blob/master/LICENSE)
[![](https://badgen.net/badge/icon/Sponsor/pink?icon=github&label)](https://github.com/sponsors/thehale)
[![Joseph Hale's software engineering blog](https://img.shields.io/badge/jhale.dev-black.svg?style=plastic&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNCIgaGVpZ2h0PSI0IiB2aWV3Qm94PSIwIDAgMS4wNTggMS4wNTgiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PGcgY29sb3I9IiMwMDAiIHBhaW50LW9yZGVyPSJmaWxsIG1hcmtlcnMgc3Ryb2tlIj48cGF0aCBkPSJNLjY0My43NTJhLjE1Ni4xNTYgMCAwMC0uMTMuMDU5Qy40NzYuODUuNDcuOTE3LjQ2OS45M2EuMDI1LjAyNSAwIDAwLjAyNi4wMjhoLjA2NmEuMDI1LjAyNSAwIDAwLjAyNC0uMDIuMTIuMTIgMCAwMS4wMi0uMDUyQy42MTguODcuNjMyLjg2OS42NTUuODY5aC4xMjJjMC0uMDAyLjA3Ni4wMDcuMTI5LS4wNUEuMTQzLjE0MyAwIDAwLjkyOC43ODcuMDI1LjAyNSAwIDAwLjkwNi43NTJILjY0M3oiIGZpbGw9IiMwNTAiLz48cGF0aCBkPSJNLjM5My40MWEuMDIuMDIgMCAwMC0uMDIuMDJ2LjI2YzAgLjAxMi4wMDEuMDI5LS4wMTQuMDQ0Qy4zMy43NTkuMjgyLjc1LjI2Ny43MzYuMjU3LjcyOC4yNS43MTMuMjQ0LjY4N0EuMDI1LjAyNSAwIDAwLjIyLjY3SC4xNTNhLjAyNC4wMjQgMCAwMC0uMDI1LjAyNmMuMDA0LjA1Mi4wMjUuMDkuMDUxLjExOWEuMTY3LjE2NyAwIDAwLjExMy4wNTJoLjAzNWEuMTg0LjE4NCAwIDAwLjExNS0uMDVBLjE4Mi4xODIgMCAwMC40OS42OTRWLjQzMUEuMDIuMDIgMCAwMC40Ny40MXpNLjc4Ny4zOWEuMDIuMDIgMCAwMC0uMDIuMDJ2LjI0MmMwIC4wMTEuMDA5LjAyLjAyLjAyaC4wNzdhLjAyLjAyIDAgMDAuMDItLjAyVi40MTFhLjAyLjAyIDAgMDAtLjAyLS4wMnpNLjM5My4yMThhLjAyLjAyIDAgMDAtLjAyLjAydi4wNzdjMCAuMDExLjAwOC4wMi4wMi4wMkguNDdhLjAyLjAyIDAgMDAuMDItLjAyVi4yMzhhLjAyLjAyIDAgMDAtLjAyLS4wMnpNLjU5LjFhLjAyLjAyIDAgMDAtLjAyLjAydi41MzJjMCAuMDExLjAwOS4wMi4wMi4wMmguMDc3YS4wMi4wMiAwIDAwLjAyLS4wMlYuMTJBLjAyLjAyIDAgMDAuNjY3LjF6IiBmaWxsPSIjMDBkNDAwIi8+PC9nPjwvc3ZnPg==)](https://jhale.dev)
[![](https://img.shields.io/badge/Follow-thehale-0A66C2?logo=linkedin)](https://www.linkedin.com/comm/mynetwork/discovery-see-all?usecase=PEOPLE_FOLLOWS&followMember=thehale)

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
