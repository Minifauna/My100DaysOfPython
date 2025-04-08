print(r'''
 ********************************************************************************
*                    /   \              /'\       _                              *
*\_..           /'.,/     \_         .,'   \     / \_                            *
*    \         /            \      _/       \_  /    \     _                     *
*     \__,.   /              \    /           \/.,   _|  _/ \                    *
*          \_/                \  /',.,''\      \_ \_/  \/    \                   *
*                           _  \/   /    ',../',.\    _/      \                  *
*             /           _/m\  \  /    |         \  /.,/'\   _\                 *
*           _/           /MMmm\  \_     |          \/      \_/  \                *
*          /      \     |MMMMmm|   \__   \          \_       \   \_              *
*                  \   /MMMMMMm|      \   \           \       \    \             *
*                   \  |MMMMMMmm\      \___            \_      \_   \            *
*                    \|MMMMMMMMmm|____.'  /\_            \       \   \_          *
*                    /'.,___________...,,'   \            \   \        \         *
*                   /       \          |      \    |__     \   \_       \        *
*                 _/        |           \      \_     \     \    \       \_      *
*                /                               \     \     \_   \        \     *
*                                                 \     \      \   \__      \    *
*                                                  \     \_     \     \      \   *
*                                                   |      \     \     \      \  *
*                                                    \ms          |            \ *
 ********************************************************************************
''')
print("You awaken in a cave.")
print("Your mission is to survive.")
first_choice = str(input("Do you wander further into the cave, or toward the light? Enter 'cave' or 'light':\n"))
direction = 0
final_choice = 0

if first_choice == "light":
    print(r'''
                                /^L_      ,."\
           /~\       __       /~    \   ./    \
          /   _\   _/  \     /T~\|~\_\ / \_  /~|          _^
        / \ /W  \ / V^\/X  /~         T  . \/   \    ,v-./
 ,'`-. /~   ^     H  ,  . \/    ;   .   \      `. \-'   /
     M      ~     | . ;  /         ,  _   :  .    ~\_,-'
    /    ~    .    \    /   :                   '   \   ,/`
   I o. ^    oP     '98b         -      _  9.`       `\9b.
 8oO888.  oO888P  d888b9bo. .8o 888o.       8bo.  o     988o.
 88888888888888888888888888bo.98888888bo.    98888bo. .d888P
 88888888888888888888888888888888888888888888888888888888888
 88888888888888P"   "" "   """9888P" P" "8P"   ""*9888888888
    ''')
    print("You exit the cave, greeted by a vast expanse of mountains.\n"
          "You find yourself on a small amount of flat land near a sheer cliff face.")
    print("You see a small patch of flowers between the cave entrance and the cliff face.")
    direction = str(input("Investigate the flowers, cliff face, or cave? Enter 'flowers' or 'cliff' or 'cave':\n"))


else:
    print(r'''
                       ,--.
          ,--.  .--,`) )  .--,
       .--,`) \( (` /,--./ (`
      ( ( ,--.  ) )\ /`) ).--,-.
       ;.__`) )/ /) ) ( (( (`_) )
      ( (  / /( (.' "-.) )) )__.'-,
     _,--.( ( /`         `,/ ,--,) )
    ( (``) \,` ==.    .==  \( (`,-;
     ;-,( (_) ~6~ \  / ~6~ (_) )_) )
    ( (_ \_ (      )(      )__/___.'
    '.__,-,\ \     ''     /\ ,-.
       ( (_/ /\    __    /\ \_) )
        '._.'  \  \__/  /  '._.'
            .--`\      /`--.
                 '----' 
    ''')
    print("As you shift your weight toward the darkness, you are met with a "
          "gorgonite glance and your adventure ends.\nGAME OVER")

if direction == "cave":
    print(r'''
                        ,--.
          ,--.  .--,`) )  .--,
       .--,`) \( (` /,--./ (`
      ( ( ,--.  ) )\ /`) ).--,-.
       ;.__`) )/ /) ) ( (( (`_) )
      ( (  / /( (.' "-.) )) )__.'-,
     _,--.( ( /`         `,/ ,--,) )
    ( (``) \,` ==.    .==  \( (`,-;
     ;-,( (_) ~6~ \  / ~6~ (_) )_) )
    ( (_ \_ (      )(      )__/___.'
    '.__,-,\ \     ''     /\ ,-.
       ( (_/ /\    __    /\ \_) )
        '._.'  \  \__/  /  '._.'
            .--`\      /`--.
                 '----' 
    ''')
    print("Medusa rushes from the cave and meets your glance, you are forever entombed in stone.\nGAME OVER")
elif direction == "cliff":
    print(r'''
                                   /T /I
                              / |/ | .-~/
                          T\ Y  I  |/  /  _
         /T               | \I  |  I  Y.-~/
        I l   /I       T\ |  |  l  |  T  /
     T\ |  \ Y l  /T   | \I  l   \ `  l Y
 __  | \l   \l  \I l __l  l   \   `  _. |
 \ ~-l  `\   `\  \  \\ ~\  \   `. .-~   |
  \   ~-. "-.  `  \  ^._ ^. "-.  /  \   |
.--~-._  ~-  `  _  ~-_.-"-." ._ /._ ." ./
 >--.  ~-.   ._  ~>-"    "\\   7   7   ]
^.___~"--._    ~-{  .-~ .  `\ Y . /    |
 <__ ~"-.  ~       /_/   \   \I  Y   : |
   ^-.__           ~(_/   \   >._:   | l______
       ^--.,___.-~"  /_/   !  `-.~"--l_ /     ~"-.
              (_/ .  ~(   /'     "~"--,Y   -=b-. _)
               (_/ .  \  :           / l      c"~o \
                \ /    `.    .     .^   \_.-~"~--.  )
                 (_/ .   `  /     /       !       )/
                  / / _.   '.   .':      /        '
                  ~(_/ .   /    _  `  .-<_
                    /_/ . ' .-~" `.  / \  \          ,z=.
                    ~( /   '  :   | K   "-.~-.______//
                      "-,.    l   I/ \_    __{--->._(==.
                       //(     \  <    ~"~"     //
                      /' /\     \  \     ,v=.  ((
                    .^. / /\     "  }__ //===-  `
                   / / ' '  "-.,__ {---(==-
                 .^ '       :  T  ~"   ll       
                / .  .  . : | :!        \\
               (_/  /   | | j-"          ~^
                 ~-<_(_.^-~"
    ''')
    print("As you approach the edge in search of a better view, a giant eagle in search of food notices your movement.")
    print("Her dagger-like talons pierce either side of your head and heart.\n"
          "You will be exsanguinated by the time she reaches her nest.\nGAME OVER")
elif direction == "flowers":
    print(r'''
_________________________________
 /''             "   (*
 \   %%%%%%%%          )
 /   _(>)%%%%%%       (
 \ *' /%%%%%  ,)      *)
%/   * %%%(, <(       (
 \       %% __/        *
 /&      _\ |___     /_.
 \      ( .\.'( \   /.\
         \(_.._) \.'/
          ) \__|'._/
 &&      / / )-'\
&&   ___/.' //|\ )
&&&& /._)  /.___.|
&&&&&  && (_.' \ |
&&&&&&&&   \ )  (,\
&&&&&&      \|   \ |
&&&&&&&  && |_\mrf\|
&&&&&&&&&&  | /   (/\
&&&&&&&&&___\/_____\_)___
    ''')
    print("You find a nymph among the flowers. "
          "You feel safe near her, and she can sense your distress.")
    print("The nymph offers you a choice between three wishes, "
          "you may wish for: Immortality, Freedom, or simply to go home.")
    final_choice = str(input("Enter your wish - 'immortal' or 'free' or 'home':\n"))

if final_choice == "immortal":
    print(r'''
                ...
             .####_  .
           ;#|\_|/__/|
         ;##/ / \/ \  \
        ;##/__|O||O|__ \
       ,##|/_ \_/\_/ _\ |        OOO\
       ###| | (____) | ||       OOOOO\
       ;##\/\___/\__/\ //      OOOOOOOO
      ,;####`.      \_)/       / OOOOOOO
    ;#########`. ,,,;./       /  / DOOOOOO
  .';#################;,     /  /     DOOOO
 ,######;######;;;;####;,   /  /        DOOO
;`######`'######;;;##### ,H/  /          DOOO
#`#######`;######;;### ;##H  /            DOOO
##`#######`;######## ;####H /              DOO
`#`#######`;###### ;######H/               DOO
 ###`#######`;; ;#########HH                OO
 ####`#######`;########;###H                OO
 `#####`############;'`#;##H                O
  `#####`########;' /  / `#H
   ######`#####;'  /  /   `H
   ''')
    print("The reaper has come, for only the dead cannot die.\nGAME OVER")
elif final_choice == "free":
    print("The nymph's spell leaves you feeling as though you could "
          "glide through the air with ease, weightless.")
    print("You dive, head-first, off the cliff in search of freedom.\n"
          "You attempt to control your glide, lifting your legs up from under you.")
    print("Before the first moment of weightlessness has reached your brain, "
          "you have been caught by an old hunter's noose left behind just days before.\nGAME OVER")
    print(r'''
   |/|
   | |
   |/|
   | |
   |/|
   | |
   |/|
  (___)
  (___)
  (___)
  (___)
  (___)
  // \\
 //   \\
||     ||
||     ||
||     || 
 \\___//
   ---
    ''')
elif final_choice == "home":
    print(r'''
        )
       (  (              .^.
        \) )           .'.^.'.
         (/          .'.'---'.'.
        _\)_       .'.'-------'.'.
       (__)()    .'.'-,=======.-'.'.
       (_)__)  .'.'---|   |   |---'.'.
       (__)_),'.'-----|   |   |-----'.'.
       ()__.'.'-------|___|___|-------'.'.
       (_.'.'---------------------------'.'.
       .'.'-------------------------------'.'.
      """""|====..====.=======.====..====|"""""
       ()_)|    ||    |.-----.|    ||    |
       (_)_|    ||    ||     ||    ||    |
       (...|____||____||_____||____||____|
      (_)_(|----------| _____o|----------|
      (_)(_|----------||     ||----------|
      (__)(|----------||_____||----------|
      (_)(_|---------|"""""""""|---------|
      ()()(|--------|"""""""""""|--------|
Zot-wWUwwuw|wwWWwuu|"""""""""""""|uwuwuuW|wuwwuuwu
    ''')
    print("Your pure intentions have been made clear, and the nymph simply smiles slyly "
          "at you while reality shifts around you.\n"
          "You regain a sense of self in front of your home.\nYOU WIN")
