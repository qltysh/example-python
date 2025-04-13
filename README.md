# Qlty Python Coverage Example

[Qlty](https://qlty.sh) is a Code Health Platform with support for code coverage.

This repository is an example using Qlty to track code coverage for a Python project. Coverage data is generated during the Python unit test build, and then uploaded to Qlty.

This repository uses [Coverage.py](https://coverage.readthedocs.io/) to generate the coverage data.

## Requirements

- Python 3
- Coverage.py v7 or above
- An account on [Qlty Cloud](https://qlty.sh) (free)

> [!NOTE]
>
> This repository is using GitHub's OpenID Connect (OIDC) to authenticate the coverage upload with Qlty Cloud instead of storing a coverage token as a GitHub Actions secret.

## Set up

See [`.github/workflows/main.yml`](./.github/workflows/main.yml) in this repository for a basic configuration.

## Documentation

- [Advanced code coverage configuration](https://example.com)
- [Alternative supported CI providers](https://example.com)

## Help and feedback

Join the our [Slack Community](https://example.com) for help and to provide feedback that we'll use to improve Qlty.

## License

[MIT License](./LICENSE.md)