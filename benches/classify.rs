use criterion::{criterion_group, criterion_main, Criterion};
use py3langid_rs::LanguageIdentifier;
use std::{fs, hint::black_box};

fn criterion_benchmark(c: &mut Criterion) {
    let li = LanguageIdentifier::new();
    let en = fs::read_to_string("benches/en.txt").unwrap();
    c.bench_function("en", |b| b.iter(|| li.classify(black_box(&en))));
    let zh = fs::read_to_string("benches/zh.txt").unwrap();
    c.bench_function("zh", |b| b.iter(|| li.classify(black_box(&zh))));
    let jp = fs::read_to_string("benches/jp.txt").unwrap();
    c.bench_function("jp", |b| b.iter(|| li.classify(black_box(&jp))));
}

criterion_group!(benches, criterion_benchmark);
criterion_main!(benches);
