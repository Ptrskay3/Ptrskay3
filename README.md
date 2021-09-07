Hi, I'm Peter 👋. I studied Math & Physics at University of Szeged, and graduated as a physicist in 2021. I started to learn programming in the beginning of 2018 and since then I used a broad range of tools and technologies. _To sum it up, I'm proficient with Python, JavaScript, TypeScript and Rust._ I generally love building software. I'm always looking to improve and pick up new things. Below you can find some hidden code snippets in different languages that serves as an exhaustive list about the tools I've worked with so far. You may read them if interested, or even try running some.

## Python

<details>
  <summary>Click to expand!</summary>

```python
from dataclasses import dataclass
from enum import Enum, auto
from typing import Tuple, List

class ExperienceLevel(Enum):
    BASIC = auto()
    INTERMEDIATE = auto()
    EXPERIENCED = auto()
    ADVANCED = auto()
    EXPERT = auto()

@dataclass
class Library:
    name: str
    experience_level: ExperienceLevel
    contributed: bool = False

    def __str__(self):
        return f"{self.name}: {self.experience_level.name} {'(contributed)' if self.contributed else ''}"


@dataclass
class Info:
    libs: List[Library]
    lang: Tuple[str, ExperienceLevel] = ("Python", ExperienceLevel.ADVANCED)

    def build_skill_str(self) -> str:
        return f"{self.lang[0]}: {self.lang[1].name}\n" + "\n".join(map(str, [lib for lib in self.libs]))

if __name__ == "__main__":
    info = Info([
        Library("Numpy", ExperienceLevel.ADVANCED),
        Library("Scipy", ExperienceLevel.EXPERIENCED),
        Library("Matplotlib", ExperienceLevel.EXPERIENCED, contributed=True),
        Library("Pandas", ExperienceLevel.INTERMEDIATE),
        Library("Jupyter Notebook", ExperienceLevel.ADVANCED)
        Library("Django", ExperienceLevel.BASIC),
        Library("Scikit-learn", ExperienceLevel.EXPERIENCED),
        Library("Tensorflow", ExperienceLevel.BASIC),
        Library("PyQt5", ExperienceLevel.INTERMEDIATE),
        Library("OpenCV", ExperienceLevel.BASIC)
    ])
    print(info.build_skill_str())

```

</details>

## JavaScript / TypeScript

<details>
  <summary>Click to expand!</summary>

You may run this on [CodeSandbox](https://codesandbox.io/s/skills-4u41y?file=/src/App.tsx).

```tsx
import React from "react";

interface Info {
  libs: Library[];
}

enum ExperienceLevel {
  Basic,
  Intermediate,
  Experienced,
  Advanced,
  Expert,
}

interface Library {
  name: string;
  experience_level: ExperienceLevel;
}

const info: Info = {
  libs: [
    { name: "React", experience_level: ExperienceLevel.Experienced },
    { name: "Next.js", experience_level: ExperienceLevel.Intermediate },
    { name: "Node.js", experience_level: ExperienceLevel.Experienced },
    { name: "Express", experience_level: ExperienceLevel.Intermediate },
    { name: "GraphQL", experience_level: ExperienceLevel.Intermediate },
    { name: "TypeORM", experience_level: ExperienceLevel.Basic },
  ],
};

export const Skills: React.FC<{}> = () => {
  return (
    <div style={{ display: "grid", placeItems: "center" }}>
      <p>JavaScript: Experienced</p>
      <p>TypeScript: Experienced</p>
      {info.libs.map((lib) => (
        <p>{lib.name + ": " + ExperienceLevel[lib.experience_level]}</p>
      ))}
    </div>
  );
};
```

</details>

## Rust

<details>
  <summary>Click to expand!</summary>

You may run this on [Rust Playground](https://play.rust-lang.org/?version=stable&mode=debug&edition=2018&gist=d032609c288a817627627d76848fdb0d).

```rust
#[derive(Debug)]
struct Info<'a> {
    libs: Vec<Library<'a>>
}

#[derive(Debug)]
#[allow(dead_code)]
enum ExperienceLevel {
    Basic,
    Intermediate,
    Experienced,
    Advanced,
    Expert,
}

#[derive(Debug)]
struct Library<'a> {
    name: &'a str,
    exp: ExperienceLevel,
}

impl Default for Info<'_> {
    fn default() -> Self {
        let libs = vec![
            Library { name: "serde", exp: ExperienceLevel::Experienced },
            Library { name: "rayon", exp: ExperienceLevel::Experienced },
            Library { name: "pyo3", exp: ExperienceLevel::Intermediate },
            Library { name: "rocket" , exp: ExperienceLevel::Intermediate },
            Library { name: "tokio" , exp: ExperienceLevel::Intermediate },
        ];
        Info {
            libs
        }
    }
}

fn main() {
    let libs: Info = Default::default();
    println!("Rust: ExperienceLevel::Experienced");
    println!("{:#?}", libs);
}
```

</details>

## Miscellaneous

<details>
  <summary>Click to expand!</summary>
Things that would be a mistake leaving out..

## Docker

```dockerfile
FROM my_experience
COPY . .
EXPOSE Docker
ENV experience_level BASIC
RUN ["echo", "$experience_level"]
```

## PostgreSQL

```sql
SELECT lib_name, experience_level
FROM my_experience
WHERE lib_name='PostgreSQL';
```

## C#

```cs
using System;

class Experience
{
   public static string GetExperience()
   {
       throw new TimeoutException("I'm just learning C#, there's nothing fancy here yet!");
   }

   public static void Main()
   {
      GetExperience();
   }
}
```

## C

```c
#include <stdio.h>

int main(int argc, char *argv[]) {
    println("Nothing fancy here either, yet!");
}
```

## Git

```bash
git add my_experience/git &&
git commit -m "updated experience" &&
git tag -a "0.1.0" -m "first release" &&
git push --tags
```

## Linux & bash

```bash
$ history | awk 'BEGIN {FS="[ \t]+|\\|"} {print $3}' | sort | uniq -c | sort -nr | head
    178 git
    111 cd
     78 yarn
     31 cargo
     20 python3
     17 ssh
     15 exa
     14 eval
     13 rustup
     13 rg
```

## HTML & CSS

```html
<html>
  <head>
    <style>
      .experience-level {
        transform: rotateY(180deg) !important;
      }
    </style>
  </head>
  <body>
    <h1 class="experience-level">Experience level:</h1>
    <script src="../display_my_basic_experience.js"></script>
  </body>
</html>
```

## Theory, interests and others

I have experience with OOP and functional programming.
I'm familiar with data structures and algorithms.
I'm generally well-versed in math.
I have a broad interest range, currently the most exciting topics for me are: concurrent programming, Rust, probability theory, machine learning.
[According to CodersRank, I'm amongst the top 5 developer with Python, Jupyter Notebook and Rust in Hungary (which might be an overstatement if you ask me).](https://profile.codersrank.io/user/ptrskay3)

</details>
