a = gets.chomp
b = gets.chomp
c = gets.chomp

json = {
    "vertebrado" => {
        "ave" => {
            "carnivoro" => "aguia",
            "onivoro" => "pomba"
        },
        "mamifero" => {
            "onivoro" => "homem",
            "herbivoro" => "vaca"
        }
    },
    "invertebrado" => {
        "inseto" => {
            "hematofago" => "pulga",
            "herbivoro" => "lagarta"
        },
        "anelideo" => {
            "hematofago" => "sanguessuga",
            "onivoro" => "minhoca"
        }
    }
}

puts json[a][b][c]
