# Intro

# How To Use

## Install Prerequisites (MacOS M1)

1. Set up Ruby. (Do not use ruby version of System.)

    ```bash
    brew update
    brew install rbenv ruby-build
    rbenv versions
    # Got "* system (set by /Users/idong-uk/.rbenv/version)"
    rbenv install -l # Check the recent version.
    rbenv install {VERSION} && rbenv global {VERSION}
    ```

2. Add rbenv PATH in `~/.zshrc`.

    ```bash
    [[ -d ~/.rbenv  ]] && \
      export PATH=${HOME}/.rbenv/bin:${PATH} && \
      eval "$(rbenv init -)"
    ```

## Install Prerequisites (Debian Linux)

- [reference](https://jekyllrb.com/docs/installation/ubuntu/)

## Install Jekyll

1. Install jekyll.

    ```bash
    gem install bundler jekyll
    ```

2. Install gems.

    ```bash
    bundle install
    ```

3. Add webrick.

    ```bash
    bundle add webrick
    ```

4. Set up [jekyll-plantuml](https://github.com/yegor256/jekyll-plantuml/tree/master?tab=readme-ov-file)

    ```bash
    sudo apt-get update
    sudo apt-get install graphviz

    mkdir -p /opt/local/bin
    ln -s /usr/bin/dot /opt/local/bin/dot

    wget https://github.com/plantuml/plantuml/releases/download/v1.2024.0/plantuml-gplv2-1.2024.0.jar
    mv plantuml-gplv2-1.2024.0.jar /opt/local/bin/plantuml.jar
    chmod 777 /opt/local/bin/plantuml.jar
    java -jar /opt/local/bin/plantuml.jar -testdot

    cat <<EOF > /usr/local/bin/plantuml
    #!/bin/bash
    java -jar /opt/local/bin/plantuml.jar "\$1" "\$2"
    EOF
    chmod +x /usr/local/bin/plantuml
    ```

## Build

```bash
bundle exec jekyll build
```

## Serve

```bash
bundle exec jekyll serve
```

Then, open `http://localhost:4000` on web browser.
