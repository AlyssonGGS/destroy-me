__author__ = 'AlyssonNote'
class PhysicManager():
    mult = 2.7 # uma gambiarra que eu fiz para nao ficar mudando 200000 de valores toda hora. Est� funcionando bem
    def __init__(self):
        return

    def gravity(self,deltaT,gameObjects):#metodo s� recebera objectos dinamicos. Provavelmente nao receber� o tiro
        for gameObject in gameObjects:#para cada Game Object
            gameObject.y += gameObject.gravity * deltaT * self.mult#aplica a for�a no Y  do Game Object para faze-lo descer
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
                        if brick.y >  player.y + player.height * 0.5:
                            player.y = brick.y - player.height#sera mutavel
                            player.canJump = True#habilita o pulo do player
                            player.gravity = 0#restaura o valor da gravidade
                            player.jumpForce = 0
                        else:
                            if player.jumpForce == 0:
                                if player.x + player.width > brick.x and player.x < brick.x:
                                    player.x = brick.x - player.width
                                else:
                                    player.x = brick.x + brick.width

        return

    def playerMove(self,deltaT,player):#movimenta os jogadores de acordo com os inputs. Ver metodo input do player
        player.x += player.move * player.velocity * deltaT
        return

    def collisionPlayerVSBall(self,players,ball):
        for player in players:
            if player.image.collided(ball.image):
                return True
        return

    def applyJump(self,deltaT,player):#aplica o efeito de pulo no jogador
        if player.jumpForce > 0:#caso o player tenha alguma for�a para pular
            player.y -= player.jumpForce * deltaT * self.mult#modifica o Y do player de acordo com a for�a do pulo
            player.jumpForce -= player.jumpForce * deltaT * self.mult#modifica a for�a do pulo
        return

    def shotMove(self,shot,dt):
        if shot.force > 0:
            shot.x += shot.direction[0] * dt * shot.force
            shot.y -= shot.direction[1] * dt * shot.force
            shot.force -= dt * 5
        return