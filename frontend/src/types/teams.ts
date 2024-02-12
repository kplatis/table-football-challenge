import { Player } from '@/types/players'

export type Team = {
  id: number
  name: string
  first_player: Player
  second_player?: Player
}
