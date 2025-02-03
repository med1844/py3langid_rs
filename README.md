# `py3langid_rs`

This is a pure-rust port of [`py3langid`](https://github.com/adbar/py3langid) with less functionalities (e.g. no server, no probability normalization, no language set).

## Build

Normally you don't have to do anything.

<details>
  <summary>In case you need to convert pickle...</summary>

The converted model is uploaded to git, thus normally you don't have to do this. Only do this when there's a model update in the upstream.

---

There's no easy way to directly load the original pickle. Thus, we must convert the pickle first.

### Set up environment

I'm using `uv` here due to it's super fast speed, you can also use other package managers.

```bash
uv venv
uv sync
```

### Run conversion script

```bash
uv run convert_pkl.py
```

This would automatically create a file `model.bin` in folder `resource/`.

</details>

## Usage

Add to your project:

```bash
cargo add py3langid_rs
```

Example usage:

```rust
use py3langid_rs::LanguageIdentifier; 

fn main() {
    let li = LanguageIdentifier::new();
    println("{:?}", li.classify("This text is in English."));
}
```

Code above should print `("en", -56.77429)`.

### Performance

Expected to be 30x faster than py3langid.

