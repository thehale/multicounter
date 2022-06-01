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
This project ships with a VS Code
["devcontainer"](https://code.visualstudio.com/docs/remote/create-dev-container)
to provide you with the easiest possible environment setup.

1. Make sure you have both [Docker](https://docs.docker.com/get-docker/) and [VS
Code](https://code.visualstudio.com/) (including the [Remote Containers
Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers))
installed on your machine.

2. [Make your own fork](https://github.com/python-poetry/poetry/fork) of
   `MultiCounter`

3. Clone the source code of `MultiCounter` onto your machine and open it in VS
   Code
   - Make sure to replace `YOUR_GITHUB_USERNAME` in the command below with your
     actual GitHub username!
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/multicounter.git
cd multicounter
code .
```

4. Accept the prompt from VS Code to **Reopen in Container**.
    - If you don't see this pop-up, go to `View` -> `Command Palette` ->
    `Remote-Containers: Open Folder in Container`
    - Note that the devcontainer may take several minutes to load for the first
    time. Successive launches will be much faster.


5. Run the unit tests to make sure everything is working.
```bash
poetry run pytest
```

## Submitting Contributions
After completing the installation steps above, make whatever bug fixes or
improvements you want in the codebase.

When you are done, simply commit your code with a brief message explaining what
was changed, and why. A series of automated checks will run to make sure
everything looks good before the commit gets saved:
- The unit test suite will automatically run and inform you of any failing tests
  that need fixing.
- Linters will automatically run and correct any code formatting problems. Make
  sure to `git add .` after these run to capture their changes.

Finally push up your changes to your fork and open a Pull Request (PR) back into
`jhale1805/multicounter`.
- A bot will post a link on your PR asking you to sign a standard Contributor
  License Agreement (CLA) giving me permission to integrate your contribution
  into the project.
- Any questions about your contribution will be discussed within the PR's
  comment section.
- After everything looks great, your PR will be merged into the `main` branch of
  `MultiCounter`!

## Other Useful Information

You can easily update the project dependencies using Poetry.
```bash
poetry update
```
