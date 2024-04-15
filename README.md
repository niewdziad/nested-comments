# nested-comments

def print_comments(comments, indent=0): - Definiuje funkcję print_comments z dwoma parametrami: comments, który jest słownikiem komentarzy, i opcjonalnym indent, który określa poziom wcięcia.

if "value" in comments: - Sprawdza, czy w słowniku comments istnieje klucz "value", co oznacza obecność komentarza.

print("->" + " " * indent + comments["value"]) - Jeśli klucz "value" istnieje, drukuje wartość komentarza z odpowiednim wcięciem, które składa się z strzałki "->" oraz spacji pomnożonych przez wartość indent.

if "subcomments" in comments: - Sprawdza, czy w bieżącym komentarzu istnieje klucz "subcomments", który zawiera listę podkomentarzy.

for subcomment in comments["subcomments"]: - Jeśli istnieją podkomentarze, przechodzi przez każdy z nich.

print_comments(subcomment, indent + 3) - Rekurencyjnie wywołuje funkcję print_comments dla każdego podkomentarza, zwiększając poziom wcięcia o 3 dla każdego kolejnego poziomu komentarza.

Na końcu, gdy kod jest wywoływany z przykładowym słownikiem comments, funkcja print_comments drukuje komentarze i podkomentarze w odpowiednim formacie, przechodząc rekurencyjnie przez strukturę słownika.