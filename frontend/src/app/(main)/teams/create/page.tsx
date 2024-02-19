import TeamCreationForm from '@/components/teams/TeamCreationForm'
import { Title } from '@mantine/core'

export default function TeamCreationPage() {
  return (
    <>
      <Title order={1} ta="center" m={'xl'}>
        Create a new team
      </Title>
      <TeamCreationForm />
    </>
  )
}
