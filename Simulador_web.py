import streamlit as st
import pandas as pd
import numpy as np
from datetime import date
import time
import re
import math
from datetime import datetime, timedelta
from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from param import calcular_parametros_completos


def gerar_demanda_simulada(num_jobs, prazo):
    """
    Cria um DataFrame com a demanda de jobs simulada.
    """
    print(f"--- Gerando demanda simulada para {num_jobs} jobs ---")
    distribuicao_historica = [
            {'Ensaio': 'CIUsat', 'Tipo Amostra': 'Indeformada', 'Percentual': 34.27272727272727},
            {'Ensaio': 'CIUsat', 'Tipo Amostra': 'Deformada', 'Percentual': 22.356060606060606},
            {'Ensaio': 'CIDsat', 'Tipo Amostra': 'Indeformada', 'Percentual': 22.15909090909091},
            {'Ensaio': 'CIDsat', 'Tipo Amostra': 'Deformada', 'Percentual': 9.06060606060606},
            {'Ensaio': 'CADsat', 'Tipo Amostra': 'Deformada', 'Percentual': 1.4772727272727273},
            {'Ensaio': 'CAUsat', 'Tipo Amostra': 'Deformada', 'Percentual': 1.3787878787878787},
            {'Ensaio': 'CAUsat', 'Tipo Amostra': 'Indeformada', 'Percentual': 1.3787878787878787},
            {'Ensaio': 'CADsat', 'Tipo Amostra': 'Indeformada', 'Percentual': 1.0833333333333335},
            {'Ensaio': 'CIU', 'Tipo Amostra': 'Indeformada', 'Percentual': 0.9848484848484849},
            {'Ensaio': 'BE', 'Tipo Amostra': 'Indeformada', 'Percentual': 0.787878787878788},
            {'Ensaio': 'CID', 'Tipo Amostra': 'Indeformada', 'Percentual': 0.5909090909090909},
            {'Ensaio': 'CIDsat/GD', 'Tipo Amostra': 'Deformada', 'Percentual': 0.393939393939394},
            {'Ensaio': 'CIUsat/GD', 'Tipo Amostra': 'Deformada', 'Percentual': 0.393939393939394},
            {'Ensaio': 'BEP', 'Tipo Amostra': 'Deformada', 'Percentual': 0.29545454545454547},
            {'Ensaio': 'UUsat', 'Tipo Amostra': 'Deformada', 'Percentual': 0.29545454545454547},
            {'Ensaio': 'BE', 'Tipo Amostra': 'Deformada', 'Percentual': 0.196969696969697},
            {'Ensaio': 'PN', 'Tipo Amostra': 'Indeformada', 'Percentual': 0.196969696969697},
            {'Ensaio': 'UUsat', 'Tipo Amostra': 'Indeformada', 'Percentual': 0.196969696969697},
            {'Ensaio': 'BEP', 'Tipo Amostra': 'Indeformada', 'Percentual': 0.1},
            {'Ensaio': 'CAU', 'Tipo Amostra': 'Deformada', 'Percentual': 0.1},
            {'Ensaio': 'CAU', 'Tipo Amostra': 'Indeformada', 'Percentual': 0.1},
            {'Ensaio': 'CCADsat', 'Tipo Amostra': 'Deformada', 'Percentual': 0.1},
            {'Ensaio': 'CCADsat', 'Tipo Amostra': 'Indeformada', 'Percentual': 0.1},
            {'Ensaio': 'RC', 'Tipo Amostra': 'Deformada', 'Percentual': 0.1},
            {'Ensaio': 'RC', 'Tipo Amostra': 'Indeformada', 'Percentual': 0.1},
            {'Ensaio': 'UU', 'Tipo Amostra': 'Deformada', 'Percentual': 0.1},
            {'Ensaio': 'UU', 'Tipo Amostra': 'Indeformada', 'Percentual': 0.1},
            {'Ensaio': 'CCIDsat', 'Tipo Amostra': 'Deformada', 'Percentual': 0.1},
            {'Ensaio': 'CCIDsat', 'Tipo Amostra': 'Indeformada', 'Percentual': 0.1},
            {'Ensaio': 'CCIUsat', 'Tipo Amostra': 'Deformada', 'Percentual': 0.1},
            {'Ensaio': 'CCIUsat', 'Tipo Amostra': 'Indeformada', 'Percentual': 0.1},
            {'Ensaio': 'EIUsat', 'Tipo Amostra': 'Deformada', 'Percentual': 0.1},
            {'Ensaio': 'EIUsat', 'Tipo Amostra': 'Indeformada', 'Percentual': 0.1},
            {'Ensaio': 'QCSD', 'Tipo Amostra': 'Deformada', 'Percentual': 0.1},
            {'Ensaio': 'QCSD', 'Tipo Amostra': 'Indeformada', 'Percentual': 0.1},
            {'Ensaio': 'CD', 'Tipo Amostra': 'Deformada', 'Percentual': 0.1},
            {'Ensaio': 'CD', 'Tipo Amostra': 'Indeformada', 'Percentual': 0.1},
            {'Ensaio': 'CS', 'Tipo Amostra': 'Deformada', 'Percentual': 0.1},
            {'Ensaio': 'CS', 'Tipo Amostra': 'Indeformada', 'Percentual': 0.1},
            {'Ensaio': 'CK0', 'Tipo Amostra': 'Deformada', 'Percentual': 0.1},
            {'Ensaio': 'CK0', 'Tipo Amostra': 'Indeformada', 'Percentual': 0.1},
            {'Ensaio': 'CCAUsat', 'Tipo Amostra': 'Deformada', 'Percentual': 0.1},
            {'Ensaio': 'CCAUsat', 'Tipo Amostra': 'Indeformada', 'Percentual': 0.1},
    ]
    df_dist = pd.DataFrame(distribuicao_historica)
    df_dist['Probabilidade'] = df_dist['Percentual'] / df_dist['Percentual'].sum()

    indices_sorteados = np.random.choice(df_dist.index, size=num_jobs, p=df_dist['Probabilidade'])
    df_sorteado = df_dist.loc[indices_sorteados].reset_index(drop=True)

    # Gera datas aleatórias dentro de um período d
    random_days = np.random.randint(0, prazo_dias, size=num_jobs)
    datas_inicio = random_days

    df_simulado = pd.DataFrame({
        "ID Ensaio/CP": range(num_jobs),
        "Campanha": "Simulada",
        "Amostra": [f"Amostra_Sim_{i}" for i in range(num_jobs)],
        "Nome Amostra": np.random.choice(['Argila arenosa', 'Silte argiloso', 'Areia siltosa'], size=num_jobs),
        "Tipo Amostra": df_sorteado["Tipo Amostra"],
        "Ensaio": df_sorteado["Ensaio"],
        "Início Plan Atual": datas_inicio,
        "Especificação Técnica Ensaio": "Deformação: 20%"
    })
    return df_simulado



# =========================================================================
#                   CONFIGURAÇÃO INICIAL DA PÁGINA
# =========================================================================
st.set_page_config(
    page_title="Simulador de Capacidade",
    layout="wide",
    page_icon="CHMMS_icone-34.png",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "Simulador de Capacidade desenvolvido para o Laboratório Central."
    }
)

# =========================================================================
#                   ESTILIZAÇÃO CSS (CORES DA IMAGEM)
# =========================================================================
def aplicar_estilo_personalizado():
    """
    Injeta CSS para estilizar a aplicação com as cores desejadas.
    """
    # Cores extraídas da imagem de referência
    cor_fundo_sidebar = "#2A3946"  # Azul escuro/ardósia
    cor_fundo_principal = "#FFFFFF" # Branco
    cor_texto = "#D1D5F5"
    cor_texto_claro = "#FFFFFF"
    cor_botao = "#3E5060" # Tom de azul um pouco mais claro para botões
    cor_botao_hover = "#5A728A" # Cor do botão ao passar o mouse
    cor_rotulo_sidebar = "#CED4DA"

    # Código CSS para ser injetado na página
    estilo_css = f"""
        <style>
            /* Estilo da barra lateral (sidebar) */
            [data-testid="stSidebar"] {{
                background-color: {cor_fundo_sidebar};
                color: {cor_texto_claro};
            }}

            [data-testid="stSidebar"] .st-emotion-cache-17lnt2j, 
            [data-testid="stSidebar"] .st-emotion-cache-6qob1r {{
                color: {cor_texto_claro};
            }}

            /* Estilo do botão primário */
            .stButton > button {{
                background-color: {cor_botao};
                color: {cor_texto_claro};
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
            }}

            /* Altera a cor da barra preenchida do slider */
            [data-testid="stSlider"] div[data-baseweb="slider"] div[style*="background: rgb(255, 75, 75);"] {{
                background-color: {cor_botao} !important;
            }}

            /* Altera a cor da bolinha (thumb) do slider */
            [data-testid="stSlider"] div[role="slider"] {{
                background-color: {cor_botao} !important;
            }}

            /* Altera a cor do valor (ex: 10%) que aparece acima da bolinha */
            [data-testid="stThumbValue"] {{
                 color: {cor_botao} !important;
            }}
            
            /* Cor dos RÓTULOS (labels) dos widgets na sidebar */
            [data-testid="stSidebar"] label {{
                color: {cor_rotulo_sidebar};
            }}
            
            .stButton > button:hover {{
                background-color: {cor_botao_hover};
                color: {cor_texto_claro};
                border: none;
            }}
            .stButton > button:active {{
                background-color: {cor_botao};
                color: {cor_texto_claro};
                border: none;
            }}

            /* Estilo geral da página */
            .main .block-container {{
                padding-top: 2rem;
            }}
            h1, h2, h3 {{
                color: {cor_texto};
            }}
            :root {{
                --primary: {cor_botao};
                --text-color: {cor_texto_claro};
                --primary-hover: #5A728A; /* Define a cor para o estado hover */
            }}
            
        </style>
    """
    st.markdown(estilo_css, unsafe_allow_html=True)

# Aplica o estilo no início da execução do script
aplicar_estilo_personalizado()

# =========================================================================
#                   INTERFACE DO USUÁRIO (UI)
# =========================================================================

# --- BARRA LATERAL (SIDEBAR) ---
with st.sidebar:
    try:
        st.image("CHMMS_logo_reduzida-16.png", width=180)
    except Exception as e:
        st.warning("Arquivo 'logo.png' não encontrado. Coloque o logo na pasta do projeto.")
    
    st.title("Configuração da Simulação")
    st.markdown("---")

    # --- 1. SELEÇÃO DA CATEGORIA DE ENSAIO ---
    categorias_de_ensaio = ["", "Compressão Triaxial"] 
    categoria_selecionada = st.selectbox(
        "Categoria de Ensaio:",
        options=categorias_de_ensaio
    )

# --- PÁGINA PRINCIPAL ---
st.title("Simulador de Capacidade do Laboratório Central")

def calcular_total_recursos(config):
    return sum(v for k, v in config.items())

if categoria_selecionada == "Compressão Triaxial":

    capacidade_inicial = {
        'BANCADA_PREP_ATIVA': 1, 'BANCADA_TARUGO': 3, 'BANCADA_MONTAGEM': 3,
        'LINHA_SAT_CO2': 1, 'BANCADA_DESM': 1,
        'PRENSA_ESPECIAL_ANISO_CICLICO': 1, 'PRENSA_ROMP_ISO': 8,
        'BANCADA_ADEN_CONVENCIONAL': 6, 'PAINEL_SAT_H2O': 60, 'PAINEL_SAT_CP': 12,
        'CELULA_CONVENCIONAL': 55, 'CELULA_CICLICO': 2, 'CELULA_BENDER': 2
    }
    
    st.header("Parâmetros para Compressão Triaxial")
    
    col1, col2 = st.columns(2)

    with col1:
        quantidade_jobs = st.number_input("Quantidade de ensaios:", min_value=1, max_value=5000, value=576, step=1)
        prazo_dias = st.number_input("Prazo ideal (dias):", min_value=1, max_value=365, value=30, step=1)

    with col2:
        num_simulacoes = st.number_input("Número de simulações:", min_value=1, max_value=10, value=2, step=1)
        tolerancia_prazo = st.slider("Tolerância no prazo (%):", min_value=0, max_value=50, value=5, step=1, format="%d%%")

    st.markdown("---")
    
    iniciar_simulacao = st.button("Iniciar Dimensionamento", type="primary", use_container_width=True)

    if iniciar_simulacao:
        st.info("Iniciando a simulação... Por favor, aguarde.")
        barra_de_progresso = st.progress(0, text="Inicializando...")
        
        recurso_final_tracker = None
        makespan_final_tracker = float('inf')
        total_recursos_da_melhor_config_tracker = float('inf')

        soma_makespan = 0.0
        soma_makespan_real = 0.0
        soma_recursos = defaultdict(int)
        soma_gargalo = pd.DataFrame()
        soma_gargalo_real = pd.DataFrame()
        num_melhores_encontrados = 0

        for i in range(num_simulacoes):
            barra_de_progresso.progress(i / num_simulacoes, text=f"Executando Simulação Mestra {i+1}/{num_simulacoes}...")
            
            df = gerar_demanda_simulada(quantidade_jobs,prazo_dias)
            recursos_1, makespan_1, gargalo, makespan_real, gargalo_real = calcular_parametros_completos(df, prazo_dias, tolerancia_prazo/100, 5 + num_simulacoes)
            total_recursos_atual = calcular_total_recursos(recursos_1)

            soma_makespan_real+=makespan_real
            if soma_gargalo_real.empty:
                soma_gargalo_real = gargalo_real.set_index('Recurso')
            else:
                # Alinha os DataFrames pelo 'Recurso' e soma apenas as colunas numéricas
                soma_gargalo_real = soma_gargalo_real.add(gargalo_real.set_index('Recurso'), fill_value=0)


            # Lógica para determinar se a configuração da simulação atual é a "melhor" até agora
            if recurso_final_tracker is None or \
               makespan_1 < makespan_final_tracker - 1.5 or \
               (abs(makespan_1 - makespan_final_tracker) < 1.5 and total_recursos_atual < total_recursos_da_melhor_config_tracker):
                
                # Atualiza o tracker da melhor configuração
                recurso_final_tracker = recursos_1.copy()
                makespan_final_tracker = makespan_1
                total_recursos_da_melhor_config_tracker = total_recursos_atual
                
                # --- ACUMULA OS VALORES PARA A MÉDIA ---
                print(f"  --> Nova melhor configuração encontrada na simulação {i+1}. Acumulando para média.")
                num_melhores_encontrados += 1
                soma_makespan += makespan_1
                for recurso, quantidade in recursos_1.items():
                    soma_recursos[recurso] += quantidade
                
                if soma_gargalo.empty:
                    soma_gargalo = gargalo.set_index('Recurso')
                else:
                    # Alinha os DataFrames pelo 'Recurso' e soma apenas as colunas numéricas
                    soma_gargalo = soma_gargalo.add(gargalo.set_index('Recurso'), fill_value=0)
                # ---------------------------------------
        barra_de_progresso.progress(100, text="Simulação concluída!")
        st.success("Dimensionamento concluído com sucesso!")
        
        # --- INÍCIO DA EXIBIÇÃO DOS RESULTADOS ---
        st.markdown("---")
        st.header("Resultados do Dimensionamento")

        if num_melhores_encontrados > 0:
            # Calcular as médias
            makespan_medio = soma_makespan / num_melhores_encontrados
            #Makespan médio da configuração real para cada instância de dados
            makespan_real_medio = soma_makespan_real/num_simulacoes
            
            recursos_medios = {}
            for recurso, soma_qtde in soma_recursos.items():
                media = soma_qtde / num_melhores_encontrados
                recursos_medios[recurso] = math.ceil(media) # Arredonda para cima
            #Gargalo para a nova configuração sugerida
            gargalo_medio = soma_gargalo.divide(num_melhores_encontrados).reset_index()
            gargalo_medio['Score_Gargalo'] = gargalo_medio['Tempo_Espera'] * (gargalo_medio['Utilizacao']/100)

            #Comportamento dos gargalos para a configuração atual do sistema
            gargalo_medio_real = soma_gargalo_real.divide(num_simulacoes).reset_index()
            gargalo_medio_real['Score_Gargalo'] = gargalo_medio_real['Tempo_Espera'] * (gargalo_medio_real['Utilizacao']/100)


            col_inicial, col_otimizada = st.columns(2)

            with col_inicial:
                # Mostra o resultado com a configuração de recursos inicial
                st.metric(
                    label="Prazo Estimado (Config. atual)",
                    value=f"{makespan_real_medio / 24:.1f} dias"
                )

            with col_otimizada:
                # Calcula a diferença em dias
                diferenca_dias = (makespan_medio / 24) - (makespan_real_medio / 24)
                
                # Mostra o resultado com a configuração otimizada e a melhoria
                st.metric(
                    label="Prazo Recomendado (Config. Otimizada)",
                    value=f"{makespan_medio / 24:.1f} dias",
                    delta=f"{diferenca_dias:.1f} dias",
                    # "inverse" colore o delta de verde se for negativo (melhora)
                    # e de vermelho se for positivo (piora).
                    delta_color="inverse" 
                )

            # Exibir a tabela com a configuração de recursos recomendada
            st.subheader("Configuração de Recursos Recomendada")
            # 1. Criar os DataFrames
            df_inicial = pd.DataFrame(list(capacidade_inicial.items()), columns=['Recurso', 'Quantidade Inicial'])
            df_media = pd.DataFrame(list(recursos_medios.items()), columns=['Recurso', 'Quantidade Média Recomendada'])

            # 2. Unir os dois DataFrames
            df_comparativo = pd.merge(df_inicial, df_media, on='Recurso', how='left').fillna(0)

            # 3. Exibir a tabela comparativa COMPLETA (sem filtro)
            st.dataframe(df_comparativo.sort_values(by='Recurso').reset_index(drop=True), use_container_width=True)

            # 4. GERAR E EXIBIR O GRÁFICO DE BARRAS COM TODOS OS RECURSOS
            st.write("#### Visualização do Comparativo de Todos os Recursos")

            # Prepara o DataFrame para o gráfico, usando 'Recurso' como índice para os rótulos
            df_para_plotar = df_comparativo.set_index('Recurso').sort_index()
            # Ordena o DataFrame pela coluna 'Quantidade Média Recomendada', do maior para o menor
            df_para_plotar = df_para_plotar.sort_values(by='Quantidade Média Recomendada', ascending=False)

            fig, ax = plt.subplots(figsize=(14, 8)) # Aumentei um pouco o tamanho para caber mais rótulos

            # Posições das barras no eixo X
            x = np.arange(len(df_para_plotar.index))
            width = 0.4  # Largura das barras

            # Cores
            cor_inicial = "#BCCCFF"
            cor_recomendada = "#054D8B"

            # Plotar as barras
            rects2 = ax.bar(x - width/2, df_para_plotar['Quantidade Média Recomendada'], width, label='Recomendada', color=cor_recomendada)
            rects1 = ax.bar(x + width/2, df_para_plotar['Quantidade Inicial'], width, label='Quantidade Inicial', color=cor_inicial)


            # Adicionar textos, título e labels
            ax.set_ylabel('Quantidade de Unidades')
            ax.set_title('Comparativo de Capacidade de Todos os Recursos: Inicial vs. Recomendada')
            ax.set_xticks(x)
            ax.set_xticklabels(df_para_plotar.index, rotation=60, ha="right") # Rotação maior para melhor visualização
            ax.legend()
            ax.grid(axis='y', linestyle='--', alpha=0.7)

            # Adicionar rótulos de dados acima das barras
            ax.bar_label(rects1, padding=3, fmt='%d')
            ax.bar_label(rects2, padding=3, fmt='%d')

            fig.tight_layout()
            st.pyplot(fig)

            # Exibir a análise de gargalo da melhor configuração encontrada
            st.subheader("Análise de Desempenho Média da Configuração Recomendada")
            # 1. ORDENA o DataFrame com os dados numéricos primeiro, do maior para o menor
            gargalo_medio_ordenado = gargalo_medio.sort_values(by='Score_Gargalo', ascending=False).reset_index(drop=True)

            # 2. Cria uma cópia para formatação
            gargalo_medio_formatado = gargalo_medio_ordenado.copy()

            # 3. FORMATA as colunas para uma exibição amigável
            gargalo_medio_formatado['Utilizacao'] = gargalo_medio_formatado['Utilizacao'].map('{:,.1f}%'.format)
            gargalo_medio_formatado['Tempo_Espera'] = gargalo_medio_formatado['Tempo_Espera'].map('{:,.1f} h'.format)
            gargalo_medio_formatado['Score_Gargalo'] = gargalo_medio_formatado['Score_Gargalo'].map('{:,.2f}'.format)

            # 4. EXIBE o DataFrame já ordenado e formatado
            st.dataframe(gargalo_medio_formatado, use_container_width=True)

            st.markdown("---")
            st.header("Análise Comparativa de Desempenho")

            # Presume-se que 'df_gargalo_real' e 'gargalo_medio_ordenado' já existem.

            # 1. Preparar os dados para os gráficos
            df_analise_inicial = gargalo_medio_real.set_index('Recurso')
            df_analise_otimizada = gargalo_medio_ordenado.set_index('Recurso')

            # Unir os dados de utilização
            df_utilizacao_comp = pd.concat([
                df_analise_inicial['Utilizacao'], 
                df_analise_otimizada['Utilizacao']
            ], axis=1, keys=['Inicial', 'Otimizada']).fillna(0)
            df_utilizacao_comp = df_utilizacao_comp.sort_values(by='Inicial', ascending=False)

            # Unir os dados de tempo de espera
            df_espera_comp = pd.concat([
                df_analise_inicial['Tempo_Espera'], 
                df_analise_otimizada['Tempo_Espera']
            ], axis=1, keys=['Inicial', 'Otimizada']).fillna(0)
            df_espera_comp = df_espera_comp.sort_values(by='Inicial', ascending=False)



            # 2. GRÁFICO 1: TAXA DE UTILIZAÇÃO
            st.write("#### Comparativo de Taxa de Utilização Média")
            fig_util, ax_util = plt.subplots(figsize=(16, 10)) # Ajustei o tamanho para melhor visualização horizontal

            # Posições das barras no eixo Y
            y = np.arange(len(df_utilizacao_comp.index))
            height = 0.35  # Agora é a altura (espessura) da barra

            # Cores
            cor_inicial = "#BCCCFF"
            cor_otimizada = "#054D8B"

            # Plotar as barras horizontais (barh)
            rects1 = ax_util.barh(y + height/2, df_utilizacao_comp['Inicial'], height, label='Utilização Inicial', color=cor_inicial)
            rects2 = ax_util.barh(y - height/2, df_utilizacao_comp['Otimizada'], height, label='Utilização Otimizada', color=cor_otimizada)

            # Adicionar textos, título e labels (eixos trocados)
            ax_util.set_xlabel('Taxa de Utilização (%)')
            ax_util.set_ylabel('Recursos')
            ax_util.set_title('Taxa de Utilização Média: Configuração Inicial vs. Otimizada')
            ax_util.set_yticks(y)
            ax_util.set_yticklabels(df_utilizacao_comp.index)
            ax_util.invert_yaxis()  # Para manter o recurso de maior utilização no topo
            ax_util.legend()
            ax_util.grid(axis='x', linestyle='--', alpha=0.7) # Grid agora no eixo X

            # Adicionar rótulos de dados ao lado das barras
            ax_util.bar_label(rects1, padding=3, fmt='%.1f%%')
            ax_util.bar_label(rects2, padding=3, fmt='%.1f%%')

            fig_util.tight_layout()
            st.pyplot(fig_util)


            # 3. GRÁFICO 2: TEMPO DE ESPERA

            # 1. Calcular os totais de tempo de espera
            total_espera_inicial = df_espera_comp['Inicial'].sum()
            total_espera_otimizada = df_espera_comp['Otimizada'].sum()

            # 2. Calcular a diferença
            diferenca_espera = total_espera_otimizada - total_espera_inicial

            # 3. Exibir os KPIs em colunas
            col_espera1, col_espera2 = st.columns(2)
            with col_espera1:
                st.metric(
                    label="Espera Total (Config. Inicial)",
                    value=f"{total_espera_inicial:.0f} horas"
                )

            with col_espera2:
                st.metric(
                    label="Espera Total (Config. Otimizada)",
                    value=f"{total_espera_otimizada:.0f} horas",
                    delta=f"{diferenca_espera:.0f} horas de redução",
                    delta_color="inverse" # Verde para valores negativos (melhora)
                )
            st.write("#### Comparativo de Tempo de Espera Gerado por Recurso")
            fig_espera, ax_espera = plt.subplots(figsize=(18, 8)) # Ajustei o tamanho

            # Posições das barras no eixo Y (usando a mesma ordem do gráfico anterior)
            y = np.arange(len(df_espera_comp.index))
            height = 0.35 # Espessura da barra

            # Plotar as barras horizontais (barh)
            rects3 = ax_espera.barh(y + height/2, df_espera_comp['Inicial'], height, label='Espera Inicial', color=cor_inicial)
            rects4 = ax_espera.barh(y - height/2, df_espera_comp['Otimizada'], height, label='Espera Otimizada', color=cor_otimizada)

            # Adicionar textos, título e labels (eixos trocados)
            ax_espera.set_xlabel('Tempo Total de Espera Gerado (horas)')
            ax_espera.set_ylabel('Recursos')
            ax_espera.set_title('Tempo de Espera Total: Configuração Inicial vs. Otimizada')
            ax_espera.set_yticks(y)
            ax_espera.set_yticklabels(df_espera_comp.index)
            ax_espera.invert_yaxis() # Mantém o recurso com maior espera no topo
            ax_espera.legend()
            ax_espera.grid(axis='x', linestyle='--', alpha=0.7) # Grid no eixo X

            # Adicionar rótulos de dados ao lado das barras
            ax_espera.bar_label(rects3, padding=3, fmt='%.0fh')
            ax_espera.bar_label(rects4, padding=3, fmt='%.0fh')

            fig_espera.tight_layout()
            st.pyplot(fig_espera)
else:
    st.info("Por favor, selecione uma categoria de ensaio na barra lateral para começar.")



