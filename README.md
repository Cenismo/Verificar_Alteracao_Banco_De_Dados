# Verificar_Alteracao_Banco_De_Dados


	Esse código compara duas abas, uma referente ao dados atualizados e outra aba com os dados do dia anterior, pois quero saber quais regras foram alteradas.

	Primeiro ele vai observar os id_rule das duas abas e capturar as linhas onde o id_rule esteja em uma aba, mas não esteja na outra (vou criar uma coluna chamada origem e mostrar de qual aba ela é).Essa é uma estrategia para poupar processamento, pois quer saber quais regras foram alterada.Sendo assim, não analizo a 'rule', pois inicialmente exigiria mais processamento. 
	
	
	Com esse novo arquivo, se a origem for aba "dia anterior", vou comparar o "id_parceiro" e "rules" com os mesmos dados na aba "dados atualizados". Se encontrar quer dizer que aquela linha não foi alterada, apenas o id, logo, não é do meu interesse. Se não for encontrado significa que a regra foi apagada ou alterada.
	

	Agora, se a origem for aba "dados atualizados", vou comparar o "id_parceiro" e "rules" com os mesmos dados na aba "dia anterior". Se encontrar quer dizer que aquela linha não foi alterada, apenas o id_rule, logo, não é do meu interesse. Significa que a regra foi alterada ou incluida.

	
	Isso tudo ficará salvo em um novo dataframe! 
