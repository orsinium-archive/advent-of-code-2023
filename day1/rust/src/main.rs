use regex::Regex;
use std::io;

fn main() {
    let rex = Regex::new(r"[^0-9]").unwrap();
    let lines = io::stdin().lines();
    let mut sum = 0;
    for line in lines {
        let line = line.unwrap();
        let line = rex.replace_all(&line, "");
        let mut chars = line.chars();
        let first = chars.next().unwrap();
        let last = chars.last().unwrap_or(first);
        let line = format!("{first}{last}");
        sum += line.parse::<i32>().unwrap();
    }
    println!("{sum}")
}
