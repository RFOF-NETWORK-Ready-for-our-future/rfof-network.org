BUBATZ-TOKEN-QUELL-CODE---S/
│
├── .github/
│   └── workflows/
│       └── build-and-run-bot.yml
├── telegram_bot.c
├── README.md
├── SECURITY.md
└── LICENSE

Here is the revised `README.md` file, incorporating the existing content and maintaining the original order of chapters:

```markdown
# BUBATZ Token Bot

Welcome to the BUBATZ Token Bot! This is a Telegram bot that provides information about the BUBATZ Token, including price, buying and selling instructions, transactions, and more. The bot is written in C and uses the `libcurl` library to send HTTP requests to the Telegram API.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Available Commands](#available-commands)
- [GitHub Actions Workflow](#github-actions-workflow)
- [Security Policies](#security-policies)
- [License](#license)

## Installation

Follow these steps to compile and run the bot locally:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/RFOF-NETWORK/BUBATZ-TOKEN-QUELL-CODE---S.git
    ```
   
2. **Navigate to the directory**:
    ```bash
    cd BUBATZ-TOKEN-QUELL-CODE---S
    ```

3. **Compile the C program**:
    ```bash
    gcc -o telegram_bot telegram_bot.c -lcurl
    ```

4. **Run the bot**:
    ```bash
    ./telegram_bot
    ```

## Usage

The bot processes various Telegram commands that provide information about the BUBATZ Token. It is designed to execute a set of predefined commands on each startup, but it can be easily customized to respond to specific user inputs.

## Available Commands

Here are the commands currently supported by the bot:

- `/start`: Greeting and overview of available commands.
- `/info`: Information about the BUBATZ Token and its goals.
- `/price`: Current token price.
- `/buy`: Instructions on how to buy tokens.
- `/sell`: Instructions on how to sell tokens.
- `/transactions`: Information on recent transactions.
- `/security`: Security tips and guidelines.
- `/support`: Contact information for support.
- `/news`: Latest news and updates about the token.
- `/community`: Information about the community and how to join.
- `/empty`: Clears the list of commands.
- `/unknown`: Notification for an unknown command.

## GitHub Actions Workflow

This repository includes a GitHub Actions workflow that automatically runs when code is pushed to the `main` branch. The workflow performs the following steps:

1. **Clone the repository**: Clones the repository onto an Ubuntu machine.
2. **Set up MSYS2**: Installs the necessary tools for compiling the C code.
3. **Compile the bot**: Compiles the Telegram bot.
4. **Run the bot**: Executes the bot.

The workflow is located in `.github/workflows/build-and-run-bot.yml`.

## Security Policies

If you discover a security vulnerability in this project, please follow these steps:

1. **Contact**: Send an email to [rfof236286@gmail.com](mailto:rfof236286@gmail.com) with details about the vulnerability.
2. **Acknowledgment**: You will receive an acknowledgment of your report within 48 hours.
3. **Assessment**: Our team will assess the vulnerability and determine its impact.
4. **Update**: You will receive updates on the progress of the fix. Our goal is to provide a solution within 7 days.
5. **Resolution**: Once the vulnerability is resolved, you will be informed, and the update will be rolled out.

## License

This project is licensed under the [MIT License](LICENSE). For more details, see the LICENSE file.

# Security Policy

## Supported Versions

Use this section to tell people about which versions of your project are currently being supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| 5.1.x   | :white_check_mark: |
| 5.0.x   | :x:                |
| 4.0.x   | :white_check_mark: |
| < 4.0   | :x:                |

## Reporting a Vulnerability

If you discover a vulnerability in this project, please follow these steps:

1. **Contact**: Send an email to [rfof236286@gmail.com](mailto:rfof236286@gmail.com) with details of the vulnerability.
2. **Acknowledgement**: You will receive an acknowledgment of your report within 48 hours.
3. **Assessment**: Our team will assess the vulnerability and determine its impact.
4. **Update**: You will receive updates on the progress of the fix. We aim to provide a fix within 7 days of reporting.
5. **Resolution**: Once the vulnerability is resolved, you will be informed, and the update will be rolled out.

Thank you for helping us keep our project secure.

# License Descriptions

## Open-Source Software Development

**GNU General Public License (GPL)**
```markdown
# GNU General Public License (GPL)

The GNU General Public License (GPL) is a free software license that ensures the end users have the freedom to run, study, share, and modify the software. The GPL requires that any modified versions of the software be distributed under the same license, preserving the same freedoms for future users.

## Key Points
- Freedom to use, study, and modify the software.
- Copyleft: Modified versions must also be open-source and licensed under GPL.
- No proprietary use.

For more details, see the full GPL text at [GNU GPL](https://www.gnu.org/licenses/gpl-3.0.html).
```

**MIT License**
```markdown
# MIT License

The MIT License is a permissive free software license that allows developers to freely use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software. It is often used for open-source projects where flexibility and simplicity are desired.

## Key Points
- Freedom to use, modify, and distribute.
- No warranty provided.
- Allows incorporation into proprietary software.

For more details, see the full MIT License text at [MIT License](https://opensource.org/licenses/MIT).
```

## Web Development and SaaS (Software as a Service)

**Apache License 2.0**
```markdown
# Apache License 2.0

The Apache License 2.0 is a permissive license with an added grant of patent rights from the contributors to the users. It allows users to freely use, modify, and distribute the software, provided that the license terms are met.

## Key Points
- Allows for use, modification, and distribution.
- Provides an explicit grant of patent rights.
- Requires attribution and preservation of notices.

For more details, see the full Apache License 2.0 text at [Apache License](https://www.apache.org/licenses/LICENSE-2.0).
```

**Creative Commons Attribution 4.0 (CC BY 4.0)**
```markdown
# Creative Commons Attribution 4.0 (CC BY 4.0)

The Creative Commons Attribution 4.0 License allows others to share, remix, adapt, and build upon the work, even commercially, as long as they credit the original creator. It is a flexible license designed for various types of works.

## Key Points
- Allows for sharing, adaptation, and commercial use.
- Requires attribution to the original creator.
- Does not impose additional restrictions.

For more details, see the full CC BY 4.0 text at [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
```

## Design and Creative Agencies

**Creative Commons Attribution-NonCommercial (CC BY-NC)**
```markdown
# Creative Commons Attribution-NonCommercial (CC BY-NC)

The Creative Commons Attribution-NonCommercial License allows others to use, remix, and build upon the work non-commercially, with credit given to the original creator. It is intended for creative works that are not intended for commercial use.

## Key Points
- Allows for non-commercial use and modification.
- Requires attribution to the original creator.
- Prohibits commercial use.

For more details, see the full CC BY-NC text at [CC BY-NC](https://creativecommons.org/licenses/by-nc/4.0/).
```

**Proprietary License**
```markdown
# Proprietary License

The Proprietary License grants specific rights to the licensee while retaining ownership of the intellectual property by the licensor. It typically includes restrictions on redistribution, modification, and usage.

## Key Points
- Grants exclusive rights to use and sometimes modify.
- Contains restrictions on redistribution and further licensing.
- Custom terms can be defined by the licensor.

For more details, see the specific terms provided by the licensor.
```

## Data Analysis and Machine Learning

**GNU Affero General Public License (AGPL)**
```markdown
# GNU Affero General Public License (AGPL)

The GNU Affero General Public License (AGPL) is a free software license designed for software that is used over a network. It requires that any modified versions of the software be made available to the public, even when used as a service.

## Key Points
- Requires disclosure of source code modifications.
- Applies to software used over a network.
- Copyleft: Modified versions must also be licensed under AGPL.

For more details, see the full AGPL text at [GNU AGPL](https://www.gnu.org/licenses/agpl-3.0.html).
```

**Open Data Commons Open Database License (ODbL)**
```markdown
# Open Data Commons Open Database License (ODbL)

The Open Database License (ODbL) allows users to freely use, modify, and distribute databases while ensuring that any derived databases are also shared under the same license.

## Key Points
- Allows for use, modification, and distribution of databases.


- Requires attribution and preservation of license.
- Derived databases must also be shared under ODbL.

For more details, see the full ODbL text at [ODbL](https://opendatacommons.org/licenses/odbl/).
```

## Pharmaceutical Research and Biotechnology

**Proprietary License with Research-Use Exception**
```markdown
# Proprietary License with Research-Use Exception

This Proprietary License allows researchers to use proprietary technologies for non-commercial research purposes while retaining commercial rights with restrictions on redistribution and modification.

## Key Points
- Grants rights for non-commercial research use.
- Restricts commercial use and redistribution.
- Custom terms are defined by the licensor.

For more details, see the specific terms provided by the licensor.
```

**Creative Commons Attribution-NonCommercial-NoDerivatives (CC BY-NC-ND)**
```markdown
# Creative Commons Attribution-NonCommercial-NoDerivatives (CC BY-NC-ND)

The Creative Commons Attribution-NonCommercial-NoDerivatives License allows others to download and share the work, but not to modify it or use it commercially. It requires attribution to the original creator.

## Key Points
- Allows sharing without modification.
- Prohibits commercial use.
- Requires attribution to the original creator.

For more details, see the full CC BY-NC-ND text at [CC BY-NC-ND](https://creativecommons.org/licenses/by-nc-nd/4.0/).
```

## Online Education and eLearning Platforms

**Creative Commons Attribution-ShareAlike (CC BY-SA)**
```markdown
# Creative Commons Attribution-ShareAlike (CC BY-SA)

The Creative Commons Attribution-ShareAlike License allows others to remix, tweak, and build upon the work, even commercially, as long as they credit the original creator and license their new creations under the identical terms.

## Key Points
- Allows for modification and commercial use.
- Requires attribution and similar licensing for derivative works.
- Promotes sharing under the same terms.

For more details, see the full CC BY-SA text at [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/).
```

**Proprietary eLearning License**
```markdown
# Proprietary eLearning License

The Proprietary eLearning License grants access to educational materials with specific restrictions on redistribution, copying, or modification. It ensures the creator's control over the use of their educational content.

## Key Points
- Grants access to educational materials.
- Imposes restrictions on redistribution and modification.
- Terms are defined by the licensor.

For more details, see the specific terms provided by the licensor.
```

## Music Production and Audio Technology

**Creative Commons Attribution-NonCommercial-ShareAlike (CC BY-NC-SA)**
```markdown
# Creative Commons Attribution-NonCommercial-ShareAlike (CC BY-NC-SA)

The Creative Commons Attribution-NonCommercial-ShareAlike License allows others to remix, tweak, and build upon the work non-commercially, as long as they credit the original creator and license their new creations under the identical terms.

## Key Points
- Allows non-commercial modification and sharing.
- Requires attribution and identical licensing for derivative works.
- Prohibits commercial use.

For more details, see the full CC BY-NC-SA text at [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/).
```

**Proprietary Music License**
```markdown
# Proprietary Music License

The Proprietary Music License grants specific rights for the use of music for commercial purposes while protecting the rights of the original artist. It often includes terms related to usage, distribution, and modification.

## Key Points
- Allows commercial use of music.
- Protects the original artist's rights.
- Custom terms defined by the licensor.

For more details, see the specific terms provided by the licensor.
```

## E-Commerce and Online Marketplaces

**GNU General Public License (GPL) for Plugins/Themes**
```markdown
# GNU General Public License (GPL) for Plugins/Themes

Plugins and themes licensed under the GNU General Public License (GPL) ensure that modifications and distributions of these components remain open-source and are licensed under the same terms as the GPL.

## Key Points
- Ensures open-source licensing for plugins and themes.
- Requires sharing of modifications under GPL.
- Compatible with various e-commerce platforms.

For more details, see the full GPL text at [GNU GPL](https://www.gnu.org/licenses/gpl-3.0.html).
```

**Proprietary License for Commercial Use**
```markdown
# Proprietary License for Commercial Use

This Proprietary License allows for the use of digital products with specific restrictions and rights defined by the licensor. It typically includes terms related to usage, redistribution, and modification.

## Key Points
- Grants specific rights for commercial use.
- Includes restrictions on redistribution and modification.
- Custom terms defined by the licensor.

For more details, see the specific terms provided by the licensor.
```
```

This format retains the original structure and chapters while ensuring clarity and organization.
