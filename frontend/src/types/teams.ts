import { Player } from '@/types/players'

export type Team = {
  id: number
  name: string
  first_player: Player
  second_player?: Player
}

export type TeamCreate = {
  name: string
  first_player_id: number
  second_player_id?: number
}