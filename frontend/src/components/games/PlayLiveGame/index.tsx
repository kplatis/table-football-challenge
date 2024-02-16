'use client'

import { useState } from 'react'
import TeamSelectionForm from '../../teams/TeamSelectionForm'
import LiveGame from './LiveGame'
import useTeams from '@/hooks/useTeams'
import { Center, Loader } from '@mantine/core'
import { FirstOrSecond, GameState } from './types'
import { notifications } from '@mantine/notifications'
import axios from 'axios'
import { GameCreationSchema } from '@/types/games'

export default function PlayLiveGame() {
  const { isLoading, data } = useTeams()

  const [step, setStep] = useState<number>(1)
  const [game, setGame] = useState<GameState>({
    firstTeam: undefined,
    secondTeam: undefined,
    firstTeamGoals: 0,
    secondTeamGoals: 0,
  })

  /**
   * Function called a team has scored. The enum parameter defines which team scored
   */
  const teamScored = (firstOrSecond: FirstOrSecond) => {
    if (firstOrSecond == FirstOrSecond.First) {
      setGame((prevGame) => ({
        ...prevGame,
        firstTeamGoals: prevGame.firstTeamGoals + 1,
      }))
    } else {
      setGame((prevGame) => ({
        ...prevGame,
        secondTeamGoals: prevGame.secondTeamGoals + 1,
      }))
    }
  }

  /**
   * Function called when the teams are selected in order to modify the state
   * @param firstTeamId
   * @param secondTeamId
   */
  const setTeams = (firstTeamId: number, secondTeamId: number) => {
    const firstTeam = data?.find((team) => team.id === firstTeamId)
    const secondTeam = data?.find((team) => team.id === secondTeamId)

    setGame((prevGame) => ({
      ...prevGame,
      firstTeam: firstTeam,
      secondTeam: secondTeam,
    }))
    setStep((prevStep) => prevStep + 1)
  }

  /**
   * Creates the game, if the game is not draw
   */
  const gameFinished = () => {
    if (game.firstTeamGoals === game.secondTeamGoals) {
      notifications.show({
        message:
          'A table football match cannot finish as a draw. Keep playing!',
      })
    } else if (game.firstTeam && game.secondTeam) {
      const data: GameCreationSchema = {
        first_team_id: game.firstTeam.id,
        second_team_id: game.secondTeam.id,
        first_team_goals: game.firstTeamGoals,
        second_team_goals: game.secondTeamGoals,
      }
      axios.post('http://localhost:8000/games', data).then((response) => {
        if (response.status === 200) {
          notifications.show({
            message: 'Success! Your game has been created.',
          })
          setGame(() => ({
            firstTeam: undefined,
            secondTeam: undefined,
            firstTeamGoals: 0,
            secondTeamGoals: 0,
          }))
          setStep(() => 1)
        }
      })
    }
  }

  if (isLoading) {
    return (
      <Center>
        <Loader color="blue" data-testid="loader" />
      </Center>
    )
  }
  if (data) {
    switch (step) {
      case 1:
        return (
          <TeamSelectionForm
            teams={data}
            setTeamsFn={setTeams}
            submissionButtonText="Start the Game!"
          />
        )
      case 2:
        return (
          <LiveGame
            game={game}
            teamScoredFn={teamScored}
            gameFinishedFn={gameFinished}
          />
        )
      default:
        return <div>test</div>
    }
  }
  return <div>Teams not fetched</div>
}
