import pygame
import sys

# Pygameの初期化
pygame.init()

# ウィンドウのサイズを定義
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# ウィンドウの作成
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Invaders")

# プレイヤーの宇宙船の画像を読み込む
player_image = pygame.image.load("player_ship.png")
player_rect = player_image.get_rect()
player_rect.centerx = WINDOW_WIDTH // 2
player_rect.bottom = WINDOW_HEIGHT - 10
# プレイヤーの宇宙船の画像を読み込む
player_image = pygame.transform.scale(player_image, (50, 50))  # 幅と高さを適切な値に変更

# 敵の宇宙船の画像を読み込む
enemy_image = pygame.image.load("enemy_ship.png")
enemy_rect = enemy_image.get_rect()
enemy_rect.centerx = WINDOW_WIDTH // 3
enemy_rect.bottom = 100  # 画面の上部から100ピクセル下に配置
enemy_image = pygame.transform.scale(enemy_image, (50,50))  # 幅と高さを適切な値に変更


# 弾の初期位置をプレイヤーの位置に設定
bullet_rect = pygame.Rect(player_rect.centerx, player_rect.top, 5, 10)

# 弾の速度
bullet_speed = 5

# ゲームループ
while True:
    # イベントの処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # キーボードの入力を取得
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 1  # 左に移動
    if keys[pygame.K_RIGHT]:
        player_rect.x += 1  # 右に移動
    if keys[pygame.K_UP]:
        player_rect.y -= 1  # 上に移動
    if keys[pygame.K_DOWN]:
        player_rect.y += 1  # 下に移動

    if keys[pygame.K_SPACE]:
        # スペースキーが押されたら弾を発射する
        bullet_rect.y -= bullet_speed

    # 弾と敵の宇宙船の当たり判定
    if bullet_rect.colliderect(enemy_rect):
    # 弾が敵の宇宙船に当たったら何らかの処理を行う
        pass

    # ウィンドウの更新
    pygame.display.update()
    # ウィンドウを黒で塗りつぶす
    window.fill((0, 0, 0))

    # プレイヤーの宇宙船を描画する
    window.blit(player_image, player_rect)

    # 敵の宇宙船を描画する
    window.blit(enemy_image, enemy_rect)

    # 画面の更新
    pygame.display.flip()

"""
1. プレイヤーの宇宙船
2. 敵の宇宙船
3. 弾の発射と当たり判定
4. スコアの計算と表示
5. ゲームオーバーの条件と終了処理

これらの要素を実装するために、Pygameの基本的な機能を使用します。例えば、画像の読み込み、イベントの処理、描画の更新などが含まれます。

プロジェクトを進める際には、次のステップを考えてみてください:

1. Pygameをインストールし、基本的なウィンドウの表示から始めます。
2. プレイヤーの宇宙船と敵の宇宙船の画像を用意し、画面上に表示します。
3. キーボードの入力を取得し、プレイヤーの宇宙船を操作します。
4. 弾の発射と当たり判定を実装します。
5. スコアの計算と表示を行います。
6. ゲームオーバーの条件と終了処理を実装します。
"""