from modelos.manga import Manga;

manga_bleach = Manga("Bleach", "74");
manga_blackclover = Manga("Black Clover", "36");

manga_bleach.alterar_estado();

manga_bleach.receber_preco("Panini", 25);
manga_blackclover.receber_preco("Panini", 22);

def main():
    Manga.listar_mangas();

if __name__ == "__main__":
    main();