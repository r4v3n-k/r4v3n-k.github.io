# Intro

This is used for the construction of my English blog.

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

3. Install jekyll.

    ```bash
    gem install bundler jekyll
    ```

4. Install gems.

    ```bash
    bundle install
    ```

## Serve

```bash
bundle exec jekyll serve
```

Then, open `http://localhost:4000` on web browser.
