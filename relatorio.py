from fpdf import FPDF

class PDF(FPDF):

    def titulo(self, label):
        self.set_font('helvetica', 'B', size=24)
        self.cell(0, 60, label, 0, 1, 'C')

    def sub_titulo(self, label):
        self.set_font('helvetica', 'I', size=16)
        self.cell(0, 10, label, 0, 1, 'C')
    
    def linha_centralizada(self, label):
        self.set_font('helvetica', '', size=12)
        self.cell(0, 10, label, 0, 1, 'C')
    
    def titulo_base(self, label):
        self.set_font('helvetica', 'B', size=16)
        self.cell(0, 8, label, 0, 1, 'L')
        self.ln()
        
    def destaque(self, label):
        self.set_font('helvetica', 'B', size=14)
        self.cell(0, 4, label, 0, 1, 'L')
        self.ln()

    def paragrafo(self, text):
        self.set_font('helvetica', '', size=12)
        self.multi_cell(0, 6, text)
        self.ln()

    def imagem(self, img, x, y, w):
        self.image(img, x, y, w)

pdf = PDF()

# ------------- Fazendo a capa -------------
pdf.add_page()

pdf.titulo("Análise da Desigualdade na Educação Brasileira")
pdf.sub_titulo("Usando dados públicos para entender problemas")
pdf.imagem("imagem_capa.png", 40, 90, 130)
pdf.ln(160)
pdf.linha_centralizada("Autora: Letícia C. Almeida")
pdf.linha_centralizada("Data: 7 de Setembro de 2024")

# ------------- 2 pagina -------------
pdf.add_page()

pdf.titulo_base("Introdução")

pdf.paragrafo("A educação é um dos pilares do desenvolvimento de uma sociedade, e sua importância pode ser percebida
no contexto do Brasil. O Brasil, um país sem litoral e com grande diversidade cultural, enfrenta grandes
desafios nos setores social, econômico e político. Portanto, a educação torna-se uma importante
ferramenta para promover a igualdade e o progresso. ")

pdf.paragrafo(" Primeiro, a educação é um direito humano, relacionado com a capacidade humana de se tornar um
cidadão pleno. O acesso a uma educação de qualidade permite que as pessoas desenvolvam as
competências e conhecimentos necessários para desempenhar um papel activo na vida política e social do
país. Isto é importante numa sociedade democrática, onde a participação dos cidadãos é crucial para a
criação de um futuro justo e equitativo.")

pdf.paragrafo(" Além disso, a educação está ligada ao desenvolvimento económico. Um país com uma população instruída
será mais inovador e competitivo no mercado global. A educação adequada ajuda a criar capital humano
qualificado, essencial para o crescimento das indústrias e dos serviços. No Brasil, investir em educação é
um investimento no desenvolvimento sustentável, porque pessoas instruídas são mais produtivas empreendedoras")

pdf.paragrafo("Outro aspecto relacionado é o papel da educação na redução das disparidades sociais. O Brasil é um dos
países com maior diversidade socioeconômica do mundo e a educação é uma das chaves para promover a
mobilidade social. Quando as crianças e os jovens, independentemente da sua origem social, têm acesso a
uma educação de qualidade, têm maior probabilidade de quebrar os ciclos de pobreza e privação. Desta
forma, a educação torna-se o motor da mudança social, permitindo às pessoas superar as barreiras
impostas pela desigualdade.")


pdf.paragrafo("Além disso, o conhecimento do nativo desenvolve habilidades críticas e reflexivas. Num mundo cheio de
informação e desinformação, é importante que as pessoas aprendam a questionar, analisar e formar as
suas próprias opiniões. Este tipo de educação ajuda a criar uma sociedade inteligente e inteligente, capaz
de enfrentar problemas e desafios com mais força.")

pdf.paragrafo("Finalmente, a promoção do conhecimento e da cultura é outra área onde o conhecimento desempenha um
papel importante. Por meio dele são preservadas e transmitidas as tradições, os valores e os conhecimentos
do povo brasileiro. Fortalece a identidade nacional e promove o respeito pela diversidade, principais
características da convivência num país tão diverso.")

pdf.paragrafo("Em resumo, a educação é importante para a sociedade brasileira devido às suas inúmeras contribuições
para o desenvolvimento humano, econômico e social. Garantir o acesso à educação de qualidade para
todos é um passo importante para tornar o Brasil melhor, mais igualitário e mais próspero. O futuro da
nação depende do seu compromisso com a educação, que é sem dúvida a base da mudança e do
progresso.")



# pdf.imagem("2_Gráfico_Cursos_por_Região.png", 30, 105, 150)
# pdf.ln(120)

# ------------- 3 pagina -------------
pdf.add_page()

pdf.titulo_base("Desenvolvimento")

pdf.destaque("1. Distribuição de Vagas")

pdf.paragrafo("Analisando a Figura 1, podemos observar as áreas mais concentradas para as regiões Sudeste e Nordeste.
Isto pode ser explicado por muitos fatores como a densidade populacional,
a presença de grandes cidades e o histórico de investimento na educação nestas áreas.
A região Sudeste tem o maior número de vagas, indicando que esta região tem mais cursos e universidades
em oferta. Esta concentração pode criar uma diferença no acesso à educação de qualidade para outrasregiões.")

pdf.imagem("Gráfico_Vagas_por_Região.png", 40, 90, 130)


# ------------- 4 pagina -------------

pdf.add_page()
pdf.destaque("2. Carga Horária Média")

pdf.paragrafo("Começando pela análise dos dados, tem-se uma visão interessante da carga horária média do curso ao
observar os gráficos abaixo.
O tempo de processamento pode variar entre diferentes regiões do país. Algumas áreas com foco
acadêmico apresentam cargas horárias mais elevadas, enquanto outras apresentam médias mais baixas.
A região também desempenha um papel importante na determinação da carga de trabalho.")


pdf.imagem("Gráfico_Carga_Horaria_por_Região.png", 40, 170, 130)

# ------------- 5 pagina -------------


pdf.destaque("3. Ensino a Distancia")

pdf.paragrafo("O gráfico de pizza abaixo mostra claramente a predominância da educação a distância no cenário
educacional brasileiro, representando 92% da oferta total de cursos. Por outro lado, o ensino presencial
representa apenas 8% do total.
O percentual significativo de educação a distância mostra uma tendência crescente de busca por essa
modalidade de ensino no Brasil. Fatores como horários flexíveis, possibilidade de estudar em qualquer lugar
e custos mais baixos podem ter motivado essa expansão")

pdf.imagem("Gráfico_Modalidade_Ensino.png", 40, 90, 130)
pdf.ln(110)

# ------------- 6 pagina -------------
pdf.add_page()

pdf.titulo_base("Conclusão")


pdf.paragrafo("A análise do caso destaca uma profunda disparidade na distribuição de vagas e na oferta de
ensino superior no Brasil, especialmente entre as regiões do país. A concentração de vagas no
Sudeste e Nordeste reflete os fatores econômicos e demográficos que fizeram com que os centros
mais poderosos se concentrassem nessas áreas.
Mas, ao mesmo tempo, a prevalência da educação a distância, que representa 92% da oferta de
cursos
, mostra uma crescente adaptação às necessidades de flexibilidade no ensino.
No entanto, a qualidade e a acessibilidade da tecnologia continuam a ser um problema,
especialmente para
sestudantes em áreas remotas e com poucos recursos.")

# ------------- 7 pagina -------------
pdf.add_page()

pdf.titulo_base("obrigada")
