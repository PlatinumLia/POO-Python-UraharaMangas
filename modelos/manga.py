from modelos.preco import Preco;

class Manga:
    mangas = [];

    def __init__(self, _nome, _volumes):
        self._nome = _nome.title();
        self._volumes = _volumes;
        self._ativo = False;
        self._preco_do_manga = [];
        self._editora = [];
        Manga.mangas.append(self);

    def __str__(self):
        return f"{self._nome} | {self._volumes} | {self.ativo}";

    @classmethod
    def listar_mangas(cls):
        print("""
            ██████████████████████████████████████████████████████████████████████▀█████████████
            █▄─██─▄█▄─▄▄▀██▀▄─██─█─██▀▄─██▄─▄▄▀██▀▄─████▄─▀█▀─▄██▀▄─██▄─▀█▄─▄█─▄▄▄▄██▀▄─██─▄▄▄▄█
            ██─██─███─▄─▄██─▀─██─▄─██─▀─███─▄─▄██─▀─█████─█▄█─███─▀─███─█▄▀─██─██▄─██─▀─██▄▄▄▄─█
            ▀▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▀▄▄▀▄▀▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▀▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀
            """);
        print(f"{"Nome do mangá".ljust(2)} | {"Volumes".ljust(2)} | {"Ativo".ljust(12)} | {"Preço total dos mangás"}");

        for manga in cls.mangas:
            print(f"{manga._nome.ljust(13)} | {manga._volumes.ljust(7)} | {manga.ativo.ljust(12)} | {int(manga.preco_medio)}");

    @property
    def ativo(self):
        return "✘ não ativo" if self._ativo else "✔ ativo";

    def alterar_estado(self):
        self._ativo = not self._ativo;

    def receber_preco(self, editora, preco_do_manga):
        preco = Preco(editora, preco_do_manga);
        self._preco_do_manga.append(preco);
    
    @property
    def preco_medio(self):
        if not self._preco_do_manga:
            return 0;
        soma_dos_precos = sum(preco._preco_do_manga for preco in self._preco_do_manga);
        quantidade_mangas = len(self._preco_do_manga);
        media = round(soma_dos_precos / quantidade_mangas, 1);
        return media;