'use client'

import { useState } from 'react'
import TeamSelectionForm from './TeamSelectionForm'
import LiveGame from './LiveGame'
import useTeams from '@/hooks/useTeams'
import { Center, Loader } from '@mantine/core'
import { FirstOrSecond, GameState } from './types'

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
  if (isLoading) {
    return (
      <Center>
        <Loader color="blue" />
      </Center>
    )
  }
  if (data) {
    switch (step) {
      case 1:
        return <TeamSelectionForm teams={data} setTeamsFn={setTeams} />
      case 2:
        return <LiveGame game={game} teamScoredFn={teamScored} />
      default:
        return <div>test</div>
    }
  }
  return <div>Teams not fetched</div>
}
