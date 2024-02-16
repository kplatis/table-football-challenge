'use client'

import { Team } from '@/types/teams'
import TeamSelectionForm from '../TeamSelectionForm'
import { useState } from 'react'
import useTeams from '@/hooks/useTeams'
import { Loader, Title } from '@mantine/core'
import StatisticsScore from '@/components/statistics/StatisticsScore'
import GameHistoryList from '@/components/games/GameHistoryList'

type TeamSelectioState = {
  firstTeam?: Team
  secondTeam?: Team
}

export default function TeamComparison() {
  const { isLoading, data } = useTeams()
  const [selectedTeams, setSelectedTeams] = useState<TeamSelectioState>({
    firstTeam: undefined,
    secondTeam: undefined,
  })

  const setSelected = (firstTeamId: number, secondTeamId: number) => {
    const firstTeam = data?.find((team) => team.id === firstTeamId)
    const secondTeam = data?.find((team) => team.id === secondTeamId)

    setSelectedTeams({
      firstTeam: firstTeam,
      secondTeam: secondTeam,
    })
  }

  if (isLoading) {
    return <Loader />
  }
  if (data) {
    return (
      <>
        <TeamSelectionForm
          teams={data}
          submissionButtonText="Compare!"
          setTeamsFn={setSelected}
        />
        {selectedTeams.firstTeam && selectedTeams.secondTeam && (
          <>
            <Title order={3} m="xl" ta="center">
              {selectedTeams.firstTeam.name} vs {selectedTeams.secondTeam.name}
            </Title>
            <StatisticsScore
              firstTeam={selectedTeams.firstTeam}
              secondTeam={selectedTeams.secondTeam}
            />
            <GameHistoryList
              firstTeam={selectedTeams.firstTeam}
              secondTeam={selectedTeams.secondTeam}
            />
          </>
        )}
      </>
    )
  }
}
