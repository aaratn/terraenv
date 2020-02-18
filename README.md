[![Actions Status](https://github.com/aaratn/terraenv/workflows/Build%20&%20Release/badge.svg)](https://github.com/aaratn/terraenv/actions)
# terraenv

![terraenv](https://repository-images.githubusercontent.com/221698182/e820d380-0bab-11ea-80b0-0f8a25a0d178
)

[Terraform](https://www.terraform.io/) & [Terragrunt](https://github.com/gruntwork-io/terragrunt) version manager inspired by [rbenv](https://github.com/rbenv/rbenv), [tfenv](https://github.com/tfutils/tfenv), [tgenv](https://github.com/cunymatthieu/tgenv)

## Support

Currently terraenv supports the following Operating System

- Mac OS X (64bit)
- Linux (64bit)

## Installation

### Automatic

Install via Homebrew on OSx

  ```console
  $ brew tap aaratn/terraenv
  $ brew install terraenv
  ```

Install via Python pip

  ```console
  $ pip install terraenv
  ```


### Upgrade

via Homebrew on OSx

  ```console
  $ brew upgrade terraenv
  ```

### Manual on Linux And OSX

1. Download terraenv for your operating system

  Linux

  ```console
  $ wget https://github.com/aaratn/terraenv/releases/latest/download/terraenv_linux_x64.tar.gz
  ```

  OSX

  ```console
  $ wget https://github.com/aaratn/terraenv/releases/latest/download/terraenv_osx_x64.tar.gz
  ```


2. Extract Tar Archive

  Linux
  ```console
  $ tar -xvzf terraenv_linux_x64.tar.gz
  ```
  OSX
  ```console
  $ tar -xvzf terraenv_osx_x64.tar.gz
  ```

3. Copy the extracted file to your `/usr/local/bin` directory

  ```console
  $ cp terraenv /usr/local/bin/terraenv
  ```

  On Ubuntu/Debian touching `/usr/local/bin` might require sudo access


## Usage

### terraenv <terraform / terragrunt > install [version]

Install a specific version of Terraform. Available options for version:

- `1.2.3` exact version to install
- `latest` installs latest version

```console
$ terraenv terraform install 0.12.15
$ terraenv terragrunt install 0.21.6
```

```console
$ terraenv terraform install latest
$ terraenv terragrunt install latest
```

### terraenv < terraform / terragrunt > list remote

#### .terraenv

If you use a [.terraenv](#.terraenv-file), `terraenv <terraform / terragrunt > install` (no argument) will install the version written in it.

### terraenv &lt;terraform/terragrunt> use &lt;version>

Switch a version to use

```console
$ terraenv terraform use 0.11.14
$ terraenv terragrunt use 0.21.6
```

### terraenv uninstall &lt;terraform/terragrunt> &lt;version>

Uninstall a specific version of Terraform

```console
$ terraenv terraform uninstall 0.12.15
$ terraenv terragrunt uninstall 0.21.5
```

### terraenv &lt;terraform/terragrunt> list local

List installed versions

```console
% terraenv terraform list local
0.12
0.11.13
0.11.14
0.12.11
0.12.0
0.12.12
0.12.13
```
```console
% terraenv terragrunt list local
0.18.7
0.21.6
```

### terraenv &lt;terraform/terragrunt> list remote

List installable versions

```console
% terraenv terraform list remote
...
0.11.3
0.11.4
0.11.5
0.11.6
0.11.7
0.11.8
0.11.9
0.11.10
0.11.11
0.11.12
0.11.13
0.11.14
0.12.0
0.12.1
0.12.2
0.12.3
0.12.4
0.12.5
0.12.6
0.12.7
0.12.8
0.12.9
0.12.10
0.12.11
0.12.12
0.12.13
0.12.14
0.12.15
```

## .terraenv file

If you put a `.terraenv` file on your project root, terraenv detects it and uses the version written in it.

```console
$ cat .terraenv
TERRAFORM=0.12.15
TERRAGRUNT=0.21.6

$ terraenv terraform install

$ terraform -version
Terraform v0.12.15

$ terraenv terragrunt install

$ terragrunt -version
terragrunt version v0.21.6

To use Terraform or Terragrunt version from `.terraenv` file present at your current directory path.

$ terraenv terraform use

$ terraenv terragrunt use
```

## LICENSE

- [terraenv](https://github.com/aaratn/terraenv/blob/master/LICENSE)
- [rbenv](https://github.com/rbenv/rbenv/blob/master/LICENSE)

## Inspiration
- [tfenv](https://github.com/tfutils/tfenv)
- [tgenv](https://github.com/cunymatthieu/tgenv)
- [rbenv](https://github.com/rbenv/rbenv)