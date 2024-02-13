'use client'

import { useState } from 'react'
import TeamSelectionForm from './TeamSelectionForm'
import LiveGame from './LiveGame'

type GameState = {
  firstTeamId?: number
  secondTeamId?: number
  firstTeamGoals: number
  secondTeamGoals: number
}

export default function PlayLiveGame() {
  const [step, setStep] = useState<number>(1)
  const [game, setGame] = useState<GameState>({
    firstTeamId: undefined,
    secondTeamId: undefined,
    firstTeamGoals: 0,
    secondTeamGoals: 0,
  })

  const setTeams = (firstTeamId: number, secondTeamId: number) => {
    setGame({ firstTeamId, secondTeamId, ...game })
    setStep(step + 1)
  }

  switch (step) {
    case 1:
      return <TeamSelectionForm setTeamsFn={setTeams} />
    case 2:
      return <LiveGame />
    default:
      return <div>test</div>
  }
}
