<!--
 Copyright (c) 2022 Joseph Hale

 This Source Code Form is subject to the terms of the Mozilla Public
 License, v. 2.0. If a copy of the MPL was not distributed with this
 file, You can obtain one at http://mozilla.org/MPL/2.0/.
-->

# Contributing to `MultiCounter`

Thank you for your interest in contributing to `MultiCounter`! This document
will guide you through setting up your development environment so you can bring
your ideas for `MultiCounter` to life.

## Development Setup

1. [Make your own fork](https://github.com/thehale/multicounter/fork) of
   `MultiCounter`

2. Clone the source code of `MultiCounter` onto your machine.
   - Make sure to replace `YOU` in the command below with your
     actual GitHub username!

    ```bash
    git clone https://github.com/YOU/multicounter.git
    cd multicounter
    code .
    ```

3. Run the setup script

    ```bash
    bin/setup.sh
    ```

4. Run the local CI checks to make sure everything is working

    ```bash
    bin/ci.sh
    ```

## Submitting Contributions
After completing the installation steps above, make whatever bug fixes or
improvements you want in the codebase.

When your bug fix/improvement is complete, run `bin/ci.sh` to verify all the quality checks.
- Fix all **FAIL**ures before submitting your contribution.
- Some issues may be autofixable via `bin/ci.sh --fix`

Finally push up your changes to your fork and open a Pull Request (PR) back into
`thehale/multicounter`.
- A bot will post a link on your PR asking you to sign a standard Contributor
  License Agreement (CLA) giving me permission to integrate your contribution
  into the project.
- Any questions about your contribution will be discussed within the PR's
  comment section.
- After everything looks great, your PR will be merged into the `main` branch of
  `MultiCounter`!
