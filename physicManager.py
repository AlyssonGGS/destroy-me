__author__ = 'AlyssonNote'
class PhysicManager():
    mult = 2.7 # uma gambiarra que eu fiz para nao ficar mudando 200000 de valores toda hora. Esta funcionando bem
    def __init__(self):
        return

    def gravity(self,deltaT,gameObjects):#metodo so recebera objectos dinamicos. Provavelmente nao recebera o tiro
        for gameObject in gameObjects:#para cada Game Object
            gameObject.y += gameObject.gravity * deltaT * self.mult #aplica a forca no Y  do Game Object para faze-lo descer
            if gameObject.gravity < 500:
                gameObject.gravity += 80 * deltaT * self.mult#aumenta o valor da gravidade
        return

    def collisionPlayerVSBricks(self,player,bricks):#colissao entre o player atual e cada bloco
        for i in range(len(bricks)):#percorre a lista de blocos
            for brick in bricks[i]:#escolhe cada bloco na lista de blocos
                if brick == None or brick.y - brick.height / 2 > player.y + player.height/2:#caso o bloco nao exista ou nao esteja a uma distancia razoavel do player
                    break#pula o teste do bloco
                else:
                    if player.image.collided(brick.image):#caso colida com o bloco
                        if brick.y > player.y + player.height * 0.8:
                            player.y = brick.y - player.height
                            player.canJump = True#habilita o pulo do player
                            player.gravity = 0#restaura o valor da gravidade
                            player.jumpForce = 0
                        else:
                            if player.jumpForce == 0:
                                if player.x + player.width > brick.x > player.x:
                                    player.x = brick.x - player.width
                                else:
                                    player.x = brick.x + brick.width

        return

    def collisionBallVsBrick(self,ball,bricks):
        for i in range(len(bricks)):
            for j in range(len(bricks[i])):
                if bricks[i][j] != None:
                    if ball.image.collided(bricks[i][j].image):
                        ball.destroy = True
                        bricks[i].pop(j)
                        return
        return

    def playerMove(self,deltaT,player):#movimenta os jogadores de acordo com os inputs. Ver metodo input do player
        player.x += player.move * player.velocity * deltaT
        return

    def collisionPlayerVSBall(self,players,ball):
        for player in players:
            if player.image.collided(ball.image):
                ball.destroy = True
                player.life -= 1
                return True
        return

    def applyJump(self,deltaT,player):#aplica o efeito de pulo no jogador
        if player.jumpForce > 0:#caso o player tenha alguma forca para pular
            player.y -= player.jumpForce * deltaT * self.mult#modifica o Y do player de acordo com a forca do pulo
            player.jumpForce -= player.jumpForce * deltaT * self.mult#modifica a forca do pulo
        return

    def shotMove(self,shot,dt):
        shot.x += shot.direction[0] * dt * shot.forceX
        shot.y -= shot.direction[1] * dt * shot.forceY
        if shot.forceY > 0:
            shot.forceY -= dt * 5
        return