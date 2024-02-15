import { Button, Group, Select, SimpleGrid, Stack } from '@mantine/core'
import { useForm } from '@mantine/form'
import {
  validateFirstTeam,
  validateSecondTeam,
} from '../../games/PlayedGameCreationForm/validation'
import { Team } from '@/types/teams'

type Props = {
  teams: Team[]
  submissionButtonText: string
  setTeamsFn: (firstTeamId: number, secondTeamId: number) => void
}

export default function TeamSelectionForm({
  teams,
  submissionButtonText,
  setTeamsFn,
}: Props) {
  const form = useForm({
    initialValues: {
      firstTeamId: null,
      secondTeamId: null,
    },
    validate: {
      firstTeamId: validateFirstTeam,
      secondTeamId: validateSecondTeam,
    },
  })

  const submit = (values: any) => {
    setTeamsFn(parseInt(values.firstTeamId), parseInt(values.secondTeamId))
  }

  const teamsData = teams.map((team) => ({
    value: team.id.toString(),
    label: team.name,
  }))

  return (
    <>
      <form onSubmit={form.onSubmit(submit)}>
        <Stack gap={'xl'}>
          <SimpleGrid cols={2}>
            <Select
              label="First Team"
              name="firstTeamId"
              placeholder="Pick a team"
              data={teamsData}
              required={true}
              data-testid="first-team-select"
              {...form.getInputProps('firstTeamId')}
            />

            <Select
              label="Second Team"
              name="secondTeamId"
              placeholder="Pick a team"
              data={teamsData}
              required={true}
              data-testid="second-team-select"
              {...form.getInputProps('secondTeamId')}
            />
          </SimpleGrid>
          <Group justify="center" mt="md">
            <Button type="submit" size="md" data-testid="teams-selected-button">
              {submissionButtonText}
            </Button>
          </Group>
        </Stack>
      </form>
    </>
  )
}
