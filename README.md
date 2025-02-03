# `py3langid_rs`

A high-performance, pure Rust implementation of language identification, ported from the Python library [`py3langid`](https://github.com/adbar/py3langid).

> [!NOTE]
> This implementation contains minimum functionalities. It lacks server, probability normalization, language subset.

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

AMD Ryzen 9 5950X, rustc 1.84.0 (9fc6b4312 2025-01-07), Ubuntu 22.04 in WSL 2.3.26.0, Windows 11 23H2.

|Implementation|Lang|Slope|Median|Mean|Std. Dev.|Speed up (Slope)|
|-|-|-|-|-|-|-|
|`py3langid_rs`|en|**29.153 µs**|29.158 µs|29.169 µs|213.92 ns|**20.954x**|
|`py3langid`|en|610.884 µs|658.544 µs|610.884 µs|161.042 µs|1.0x|
|`py3langid_rs`|zh|**14.521 µs**|14.476 µs|14.502 µs|56.782 ns|**31.296x**|
|`py3langid`|zh|454.454 µs|489.616 µs|454.454 µs|75.018 µs|1.0x|
|`py3langid_rs`|jp|**20.472 µs**|20.415 µs|20.464 µs|149.43 ns|**33.969x**|
|`py3langid`|jp|695.421 µs|747.794 µs|695.421 µs|114.144 µs|1.0x|

### Using custom model

<details>
  <summary>In case you need to convert your own model pickle...</summary>

The converted model is uploaded to git, thus normally you don't have to do this. Only do this when there's a model update in the upstream, or you have a customly trained model.

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
uv run convert_pkl.py path/to/your/model.plzma
```

This would automatically create/overwrite file `model.bin` in folder `resource/`.

</details>


