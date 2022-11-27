# Criar funções para UI
import json
import subprocess


class Init():
    def comeco(self):
        print("As suas opções são:")  # Opções de UI
        print("1 - Build")
        print("2 - List")
        print("3 - Destory")
        print("4 - Exit")


class TerraformBuild:

    def open_json(self):
        with open('vars.json') as file:
            data = json.load(file)
    
        return data

    # Execute Terraform resources
    def execute(self):
        print("Inicializando o Terraform...\n")
        subprocess.run(["terraform", "init"])
        print("Validando infra...\n")
        subprocess.run(["terraform", "validate"])
        print("Criando infra..\n")
        subprocess.run(["terraform", "apply", "-auto-approve", "-var-file=vars.json"])

    # def vpc(self):

    #     nome_vpc = input("Digite o nome da VPC: ")
    #     cidr_vpc = input("Digite o CIDR (x.x.x.x/x) da VPC: ")
        
    #     file = self.open_json()
    #     file["vpc"].append({"name": nome_vpc, "cidr": cidr_vpc})
    #     with open('vars.json', 'w') as f:
    #         json.dump(file, f, indent=4)

    # def subnet(self):

    #     nome_subnet = input("Digite o nome da Subnet: ")
    #     cidr_subnet = input("Digite o CIDR (x.x.x.x/x) da Subnet: ")

    #     # Guardar em uma variavel o arquivo json e escrever informacoes da VPC
    #     file = self.open_json()
    #     file["subnet"].append({"name": nome_subnet, "cidr": cidr_subnet})
    #     with open('vars.json', 'w') as f:
    #         json.dump(file, f, indent=4)
        
        

    # def security_group(self):

    #     nome_sg = input("Digite o nome do Security Group: ")

    #     file = self.open_json()
    #     file["security_group"].append({"name": nome_sg})
    #     with open('vars.json', 'w') as f:
    #         json.dump(file, f, indent=4)

    def instance(self):

        instance_nome = input("Digite o nome da instância: ")

        print("Tamanho da instância: ")
        print("micro")
        print("small")
        print("medium")
        print("large")
        tamanho = input("Digite o tamanho: ")
        sg = input("Digite o nome do Security Group associado à instânica: ")

        #Guardar instancias em json
        file = self.open_json()
        file["instances"].append({"name": instance_nome, "size": tamanho, "security_group": sg, "regiao": "us-east-1"})
        with open('vars.json', 'w') as f:
            json.dump(file, f,indent=4)


    def user(self):
        nome_user = input("Digite o nome do usuário: ")

        file = self.open_json()
        #print(file)
        file["user"].append(nome_user)
        with open('vars.json', 'w') as f:
            json.dump(file, f, indent=4)

        # with open('vars.json', 'w') as file:
        #     json.dump({'name': nome_user}, file)
        

class TerraformList:

    def open_json(self):
        with open('vars.json') as file:
            data = json.load(file)
        
        return data

# List terraform resources
    def list(self):

        # NÃO FUNCIONA AINDA
        if subprocess.run(["terraform", "show"]) == None:
            print("Não há recursos criados")
        else:
            subprocess.run(["terraform", "show", "-var-file=vars.json"])
    
    #Show json
    def show_json(self):
        file = open('vars.json')
        json_guardado = json.load(file)
        file.close()
        
        print(json_guardado)

    # def list_vpc(self):

    #     pass

    #     # file = open('vars.json')
    #     # json_guardado = json.load(file)
    #     # file.close()

    #     file = self.open_json()
    #     print(file["vpc"])

    #     ### Acessar o json e listar as VPCs

    # def list_subnet(self):

    #     # file = open('vars.json')
    #     # json_guardado = json.load(file)
    #     # file.close()

    #     file = self.open_json()
    #     print(file["subnet"])

        ### Acessar o json e listar as Subnets
    
    # def list_security_group(self):

    #     # file = json.load(open('vars.json'))
    #     # # Print security group name
    #     # print(file['security_group_name'])
    #     file = self.open_json()
    #     print(file["security_group"])
        

        ### Acessar o json e listar os Security Groups
    
    def list_instance(self):

        file = self.open_json()
        print(file["instances"])

        ### Acessar o json e listar as Instâncias

    def list_user(self):

        file = self.open_json()
        print(file["user"])

        ### Acessar o json e listar os Usuários



class TerraformDestroi:

# Destroy terraform resources
    def destroy(self):
        print("Destruindo recursos...\n")
        subprocess.run(["terraform", "apply", "-auto-approve", "-var-file=vars.json"])

    def load_json(self):
        with open('vars.json') as file:
            data = json.load(file)
        
        return data

    def destroy_instances(self):

        # Acessar instancias no json e selecionar qual apagar
        # Apagar instancias no json

        file = self.load_json()
        deleta_instancia = str(input("Digite o nome da instância (vai apagar security group associado também) que deseja apagar: "))
        index_to_remove = -1
        for index, instancia in enumerate(file["instances"]):
            if instancia["name"] == deleta_instancia:
                index_to_remove = index

        if index_to_remove != -1:
            file["instances"].pop(index_to_remove)
        else:
            print("Não existe instância com esse nome")

        with open('vars.json', 'w') as f:
            json.dump(file, f, indent=4)

    def destroy_users(self):

        # Acessar usuarios no json e selecionar qual apagar
        file = self.load_json()

        deleta_user = str(input("Digite o nome do usuário que deseja apagar: "))
        posicao = file["user"].index(deleta_user)
        file["user"].pop(posicao)

        with open ('vars.json', 'w') as f:
            json.dump(file, f, indent=4)        

    # def destroy_security_groups(self):

    #     file = self.load_json()
    #     deleta_sg = str(input("Digite o nome do security group que deseja apagar: "))
    #     index_to_remove = -1
    #     for index, sg in enumerate(file["security_group"]):
    #         if sg["name"] == deleta_sg:
    #             index_to_remove = index

    #     if index_to_remove != -1:
    #         file["instances"].pop(index_to_remove)
    #     else:
    #         print("Não existe security group com esse nome")

    #     with open('vars.json', 'w') as f:
    #         json.dump(file, f, indent=4)
    
    #     ### Acessar security groups no json e selecionar qual apagar
    #     pass


class TerraformQuit:
    def cabou(self):
        print("Tchau!")
        exit()

# ------------------------------------------------

# Implement funcionalities

# ------------------------------------------------


while True:
    inicio = False
    while not inicio:
        Init().comeco()
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            print("As suas opções de BUILD são: \n")
            print("1 - Instância com security group")
            print("2 - Usuário")
            print("3 - Sair\n")
            build_choice = input("Digite a opção desejada: ")
            # if build_choice == "1":

            #     # Criando VPC
            #     print("Criando VPC\n")

            #     # Executar o terraform
            #     TerraformBuild().vpc()
            #     TerraformBuild().execute()

            # elif build_choice == "2":
                
            #     # Criando Subnet
            #     print("Criando Subnet\n")

            #     # Executar o terraform
            #     TerraformBuild().subnet()
            #     TerraformBuild().execute()

            # elif build_choice == "3":

            #     print("Criando Security Group\n")
            #     TerraformBuild().security_group()
            #     TerraformBuild().execute()

            if build_choice == "1":
    
                print("Criando Instância (já com security group)\n")
                TerraformBuild().instance()
                TerraformBuild().execute()

                # Chamada de função para criar Instância

            elif build_choice == "2":

                print("Criando Usuário")

                # Chamada de função para criar Usuário
                TerraformBuild().user()
                TerraformBuild().execute()

            elif build_choice == "3":
                print("Saindo...\n")    
                exit()
            
            
        elif opcao == "2":
            
            print("As suas opções de LIST são: \n")
            # print("1 - VPC")
            # print("2 - Subnet")
            # print("3 - Security Group")
            print("1 - Instância e Security Group")
            print("2 - Usuário")
            print("3 - Sair\n")

            list_choice = input("Qual opção deseja LISTAR? ")

            # if list_choice == "1":
            #     print("Listando VPCs...\n")
            #     TerraformList().list_vpc()

            # elif list_choice == "2":
            #     print("Listando Subnets...\n")
            #     TerraformList().list_subnet()
                
            # elif list_choice == "3":
            #     print("Listando Security Groups...\n")
            #     TerraformList().list_security_group()

            if list_choice == "1":
                print("Listando Instâncias e Security Groups...\n")
                TerraformList().list_instance()

            elif list_choice == "2":
                print("Listando Usuários...\n")
                TerraformList().list_user()

            elif list_choice == "3":
                print("Saindo...")
                exit()

        elif opcao == "3":
            print("As suas opções de DESTROY são: \n")

            print("1 - Instância  e Security Group")
            print("2 - Usuário")
            # print("3 - Security Group")
            print("3 - Sair\n")

            destroy_choice = input("Qual opção deseja DESTROY? ")
            if destroy_choice == "1":
                print("Destruindo instância...\n")
                TerraformDestroi().destroy_instances()
                TerraformDestroi().destroy()
            
            elif destroy_choice == "2":
                print("Destruindo usuário...\n")
                TerraformDestroi().destroy_users()
                TerraformDestroi().destroy()

            # elif destroy_choice == "3":
            #     print("Destruindo security group...\n")
            #     TerraformDestroi().destroy_security_groups()
            #     TerraformDestroi().destroy()
            
            elif destroy_choice == "3":
                print("Saindo...")
                exit()
        elif opcao == "4":
            TerraformQuit().cabou()
        else:
            print("Opção inválida, tente novamente!")
