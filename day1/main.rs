use std::fs::read_to_string;
use std::collections::HashMap;

fn main() {
    part_one("data/data.txt");
    part_two("data/data.txt");
}

fn part_one(filename: &str) {
    let mut result: i32 = 0;
    for line in read_to_string(filename).unwrap().lines() {
        let mut first: i32 = -1;
        let mut last: i32 = -1;

        for letter in line.chars() {
            match letter.to_digit(10) {
                Some(digit) => {
                    if first == -1 {
                        first = digit as i32;
                    } else {
                        last = digit as i32;
                    }
                },
                None => continue,
            }
        }

        if last != -1 {
            result += first * 10 + last;
        } else {
            result += first * 10 + first;
        }
    }

    println!("{}", result);
}

fn part_two(filename: &str) {
    let mut result: i32 = 0;

    let numbers = HashMap::from([
        ("one", "one1one"),
        ("two", "two2two"),
        ("three", "three3three"),
        ("four", "four4four"),
        ("five", "five5five"),
        ("six", "six6six"),
        ("seven", "seven7seven"),
        ("eight", "eight8eight"),
        ("nine", "nine9nine"),
    ]);

    for line in read_to_string(filename).unwrap().lines() {
        let mut first: i32 = -1;
        let mut last: i32 = -1;

        let mut new_line = line;
        let mut tmp;

        for (key, value) in &numbers {
            tmp = new_line.replace(key, value);
            new_line = &tmp;
        }

        for letter in new_line.chars() {
            match letter.to_digit(10) {
                Some(digit) => {
                    if first == -1 {
                        first = digit as i32;
                    } else {
                        last = digit as i32;
                    }
                },
                None => continue,
            }
        }

        if last != -1 {
            result += first * 10 + last;
        } else {
            result += first * 10 + first;
        }
    }

    println!("{}", result);
}
