__author__ = 'AlyssonNote'
class PhysicManager():
    mult = 2.7 # uma gambiarra que eu fiz para nao ficar mudando 200000 de valores toda hora. Está funcionando bem
    def __init__(self):
        return

    def gravity(self,deltaT,gameObjects):#metodo só recebera objectos dinamicos. Provavelmente nao receberá o tiro
        for gameObject in gameObjects:#para cada Game Object
            gameObject.y += gameObject.gravity * deltaT * self.mult#aplica a força no Y  do Game Object para faze-lo descer
            if gameObject.gravity < 300:
                gameObject.gravity += 80 * deltaT * self.mult#aumenta o valor da gravidade
        return

    def collisionPlayerVSBricks(self,player,bricks):#colissao entre o player atual e cada bloco
        for i in range(len(bricks)):#percorre a lista de blocos
            for brick in bricks[i]:#escolhe cada bloco na lista de blocos
                if brick == None or brick.y - brick.height / 2 > player.y + player.height/2:#caso o bloco nao exista ou nao esteja a uma distancia razoavel do player
                    break#pula o teste do bloco
                else:
                    if player.image.collided(brick.image):#caso colida com o bloco
                        player.y = brick.y - player.height#sera mutavel
                        player.canJump = True#habilita o pulo do player
                        player.gravity = 0#restaura o valor da gravidade
                        player.jumpForce = 0
        return

    def playerMove(self,deltaT,player):#movimenta os jogadores de acordo com os inputs. Ver metodo input do player
        player.x += player.move * player.velocity * deltaT
        return

    def applyJump(self,deltaT,player):#aplica o efeito de pulo no jogador
        if player.jumpForce > 0:#caso o player tenha alguma força para pular
            player.y -= player.jumpForce * deltaT * self.mult#modifica o Y do player de acordo com a força do pulo
            player.jumpForce -= player.jumpForce * deltaT * self.mult#modifica a força do pulo
        return